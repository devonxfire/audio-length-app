# Audio Length Calculator

A simple desktop app and command-line tool for macOS that calculates the total length of one or more audio files (WAV/MP3). Supports drag-and-drop, multi-file selection, and a reset button. Built with Python, Tkinter, and Mutagen.

## Features
- Select multiple audio files (.wav, .mp3) and get total duration
- Drag and drop files into the app window (if `tkinterdnd2` is installed)
- Displays total length in hours, minutes, and seconds
- Shows finished hours (decimal)
- Counts valid and ignored files
- Reset button to clear results
- Works as a command-line tool (`audioLength`) or as a macOS app (via py2app)

## Installation

### Requirements
- Python 3.8+
- [Mutagen](https://pypi.org/project/mutagen/)
- [tkinterdnd2](https://pypi.org/project/tkinterdnd2/) (optional, for drag-and-drop)

Install dependencies:
```sh
python3 -m pip install mutagen tkinterdnd2
```

### Command-line Usage
1. Make the script executable:
   ```sh
   chmod +x audio_length_gui.py
   ln -s /full/path/to/audio_length_gui.py /usr/local/bin/audioLength
   ```
2. Run from anywhere:
   ```sh
   audioLength
   ```

### Build as a macOS App (optional)
1. Install py2app:
   ```sh
   python3 -m pip install py2app
   ```
2. Build:
   ```sh
   python3 setup.py py2app
   codesign --force --deep --sign - "dist/Audio Length Calculator.app"
   ```
3. Launch from Finder or with:
   ```sh
   open dist/Audio\ Length\ Calculator.app
   ```

## Usage
- Click "Open Audio Files" to select files
- Or drag and drop files into the window
- View total length, finished hours, and file counts
- Click "Reset" to clear results

## Example Output
```
Total Length: 2 Hours 23 Minutes 43 Seconds
Finished Hours: 2.40
Files counted: 3
Files ignored: 0
```

## License
MIT

---

*Created by devonxfire*
