from bs4 import BeautifulSoup
from pathlib import Path
import tomllib


def load_config(path: Path) -> Path:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    master_folder = Path(data["paths"]["master"])
    return master_folder


def extract_panels(html_path: Path) -> list[str]:
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    content_div = soup.find("div", id="content", class_="viewer")
    if content_div is None:
        return []

    panels = []
    for img in content_div.find_all("img", class_="_images"):
        src = img.get("src")
        if src:
            panel = Path(src).name
            panels.append(panel)

    return panels


def cleanup_folder(assets_path: Path, panel_list: list[str]):
    panel_set = set(panel_list)

    for path in assets_path.iterdir():
        if path.is_file() and path.name not in panel_set:
            path.unlink()

    temp_names = []
    for i, panel in enumerate(panel_list, start=1):
        old = assets_path / panel
        if not old.exists():
            continue
        tmp = assets_path / f"__tmp_{i:03d}{old.suffix}"
        old.rename(tmp)
        temp_names.append(tmp)

    for i, tmp in enumerate(temp_names, start=1):
        final = assets_path / f"{i:03d}{tmp.suffix}"
        tmp.rename(final)


def process_episode(html_path: Path, assets_path: Path):
    panels = extract_panels(html_path)
    cleanup_folder(assets_path, panels)
    html_path.unlink()
    print(f"Processed {html_path.name}, {len(panels)} panels.")


def main():
    config_path = Path(__file__).parent / "config.toml"
    master_folder = load_config(config_path)

    for html_file in master_folder.glob("EP*.html"):
        episode_name = html_file.stem
        assets_folder = master_folder / f"{episode_name}_files"
        if not assets_folder.exists():
            print(f"Warning: assets folder missing for {episode_name}")
            continue

        process_episode(html_file, assets_folder)


if __name__ == "__main__":
    main()
