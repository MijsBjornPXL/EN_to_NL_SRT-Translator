# Eng2NL_SRT_Translator


### English to Dutch Subtitle Translation and File Renaming Script

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


## Dependencies

1. **translatepy**: A Python library for translation.

   Install it with pip:
   ```bash
   pip install translatepy


Python: Make sure Python 3.x is installed.

## Installation Instructions

Clone the repository or download the script:

```bash
git clone https://github.com/MijsBjornPXL/Eng2NL_SRT_Translator.git
cd Eng2NL_SRT_Translator
```

### Run the script:

After installing the necessary dependencies, you can run the script. It will prompt you to enter the directory where your subtitle files are located.

Example:

```bash
python SubtitleTranslationScript.py
```

### Directory Structure:

The script processes files in the given directory and renames them as follows:

.en.srt files will be renamed to .nld.srt after translation.
.srt files will be renamed to .nld.srt after translation.

## Example Use Case

Place all the .en.srt and .srt subtitle files you want to translate in the same folder.
Run the script and provide the source directory.

The script will:
Process each file in chunks.
Translate the text content from English to Dutch.
Clean up the timestamps.
Save the new file with the .nld.srt extension in the same folder.
Example Input:

```plaintext
1
00:00:01,202 --> 00:00:02,436
CLAIRE: Previously on The Good Doctor...

2
00:00:02,570 --> 00:00:04,538
You don't want me to do anything.
Output: The.Good.Doctor.S04E01.1080p.WEBRip.x265-RARBG.nld.srt
```

```plaintext
Code kopiëren
1
00:00:01,202 --> 00:00:02,436
Claire: Eerder op De Goede Dokter...

2
00:00:02,570 --> 00:00:04,538
Je wilt niet dat ik iets doe.
```


## Troubleshooting

If you encounter any issues while running the script, ensure that:

The translatepy library is installed.
You have the necessary permissions to read and write to the specified directories.
If running on Windows, make sure your terminal or IDE supports UTF-8 encoding.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


