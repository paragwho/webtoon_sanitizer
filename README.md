# Webtoon Sanitizer
Extracts only the actual art panels from episodes of comics on [Webtoon](https://www.webtoons.com/en/), removing UI clutter and non-panel images.

## What does it do?
- Takes downloaded Webtoon episode pages
- Identifies and extracts only comic panels
- Outputs clean, sequentially numbered images per episode

Perfect if you want an offline, distraction-free reading experience.

## How it works
- Python
- BeautifulSoup for HTML parsing
- Hard-coded heuristics to identify real panels

No scraping Webtoon directly — it works on pages you’ve already downloaded.

## Setup
Clone the repository and install dependencies:
```
git clone https://github.com/paragwho/webtoon_sanitizer.git
cd webtoon-sanitizer
pip install .
```

## How to use
Step-by-step
1.  Open the episode(s) in a desktop browser
    - Scroll through the entire episode once (this ensures all images load)

2.  Save the page
    - Press Ctrl + S
    - Save as Webpage, Complete

3.  Name files correctly
    - HTML file: EPx.html (example: EP3.html)
    - Asset folder: EPx_files (example: EP3_files)

4.  Create a master folder
    ```
    master/
    ├─ EP1.html
    ├─ EP1_files/
    ├─ EP2.html
    ├─ EP2_files/
    ```

5.  Configure the script
    - Open [config.toml](src/config.toml)
    - Set the path to your master folder

6.  Run the script
    ```
    python main.py
    ```
    **IMPORTANT**:
    
    The script deletes the original HTML and asset files and replaces them with sanitized output. Back up your data if you want to keep the originals.

## Output
```
master/
├─ EP1_files/
│ ├─ 001.png
│ ├─ 002.png
│ └─ …
├─ EP2_files/
│ ├─ 001.png
│ ├─ 002.png
│ └─ …
```
- Only panel images remain
- Images are numbered in reading order
- Supports batch processing (EP1–EP10, EP1–EP100, etc.)

## Simple Browser Reader
### How to use
1. Copy reader.html and the icons folder into your master
folder
2. Open reader.html in any browser

### Keyboard shortcuts
| Key         | Action                  |
|-------------|-------------------------|
| ↑ / ↓       | Scroll                  |
| ← / →       | Previous / Next Episode |
| Home / End  | Jump to Top / Bottom    |
| D           | Toggle Dark Mode        |
| S           | Toggle Smooth Scrolling |

## License
This project is licensed under the [MIT License](LICENSE).
