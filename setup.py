from setuptools import setup

# Your main script
APP = ['audio_length_gui.py']

# Any additional files (none needed here)
DATA_FILES = []

# Py2app options
OPTIONS = {
    'argv_emulation': True,                 # allows drag-and-drop onto app icon
    'packages': ['mutagen', 'tkinterdnd2'], # include non-standard packages
    'includes': ['tkinter'],                # ensure tkinter is included
    'iconfile': 'icon.icns',                # your app icon
    'emulate_shell_environment': True,      # helps launch from Finder
    'plist': {
    'CFBundleName': 'Audio Length Calculator',
    'CFBundleDisplayName': 'Audio Length Calculator',
    'CFBundleIdentifier': 'com.yourname.audiolength',
    'LSMinimumSystemVersion': '10.10',
    'LSUIElement': False,               # show app normally in Dock
    },
    'excludes': ['test', 'unittest'],       # optional, to reduce size
        "argv_emulation": True,
        "emulate_shell_environment": True,
        "iconfile": "icon.icns",
        "includes": ["mutagen", "tkinterdnd2", "jaraco.text"],
        "excludes": ["PyQt5", "PySide2"],
        "plist": {
            "CFBundleName": "Audio Length Calculator",
            "CFBundleShortVersionString": "0.0.0",
            "CFBundleVersion": "0.0.0",
            "CFBundleIdentifier": "com.yourname.audiolength",
            "LSUIElement": False,
        },
    }

# Setup call
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
