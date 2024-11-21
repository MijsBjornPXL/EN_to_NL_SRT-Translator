# English to Dutch Subtitle Translation and File Renaming Script

This Python script processes subtitle files, translates them from English to Dutch, and renames the resulting files accordingly. It handles `.en.srt` and `.srt` files and uses the `translatepy` library to perform the translation.

## Features

- Processes `.en.srt` and `.srt` subtitle files in the specified directory.
- Translates the subtitle content from English to Dutch using the `translatepy` library.
- Cleans up timestamp formatting to ensure proper spacing and arrow formatting.
- Renames processed files from `.en.srt` to `.nld.srt`.
- Writes the translated subtitles to a temporary file, cleans the content, and then renames and moves the final subtitle file back to the source directory.

## Requirements

- Python 3.x
- `translatepy` for translation.
- `shutil` for file operations (comes with Python).
- `re` (comes with Python) for regular expression operations.

### Dependencies

1. **translatepy**: A Python library for translation.

   Install it with pip:
   ```bash
   pip install translatepy
