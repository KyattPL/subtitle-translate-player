# Subtitle Translator

This project allows users to translate subtitles for videos using LibreTranslate.

## Installation and Setup

### 1. Clone the Repository or Download the ZIP

To get started, clone this repository using Git:
```sh
git clone https://github.com/KyattPL/subtitle-translate-player.git
```

Alternatively, you can download the ZIP file and extract it to your desired location.

### 2. Install LibreTranslate

LibreTranslate is required for subtitle translation. Install it using `pip` inside a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\\Scripts\\activate'
pip install libretranslate
```

### 3. Start LibreTranslate

Run LibreTranslate with the required languages:
```sh
libretranslate --load-only en,es,<lang_codes>
```
Replace `<lang_codes>` with the language codes you want to support (e.g., `fr`, `de`).

## Usage

### 1. Open the Web Interface

Open `index.html` in your browser to launch the subtitle translator interface.

### 2. Load Video and Subtitle Files

- Click **Open Video** to load a video file.
- Click **Open SRT** to load the corresponding subtitle file.
- Choose the **Source Language** (detected from subtitles) and the **Target Language** (translated output).

### 3. View Translations

- Subtitles will appear as the video plays.
- Click on the subtitle text to toggle translations on/off.
- Press **Enter Fullscreen** to display subtitles over the video.

## Features
- Supports various video formats.
- Works with `.srt` subtitle files.
- Auto-detects and translates subtitles using LibreTranslate.
- Clickable subtitles to toggle translation visibility.
- Fullscreen mode with overlay subtitles.

## License
This project is open-source. Feel free to modify and improve it!