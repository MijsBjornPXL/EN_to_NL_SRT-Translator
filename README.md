# English 2 NL Translator for SRT

### English to Dutch Subtitle Translator

Translate English SRT files to Dutch!

Simple, fast, hassle-free! (No API-keys required!)

This Python script processes subtitle files, translates them from English to Dutch, and renames the resulting files accordingly. It handles `.en.srt` and `.srt` files and uses the `translatepy` library to perform the translation.
<br>

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

- **translatepy:** A Python library for translation.

   Install it with pip:
   ```bash
   pip install translatepy
<br>

**_Python: Make sure Python 3.x is installed._**
<br>
<br>

## Installation Instructions

Clone the repository or download the script:

```bash
git clone https://github.com/MijsBjornPXL/Eng2NL_SRT_Translator.git
cd Eng2NL_SRT_Translator
```

## Run the script:

After installing the necessary dependencies, you can run the script. It will prompt you to enter the directory where your subtitle files are located.

**_Example Linux:_**

```bash
python Translate_NL.py
```

**_Example Windows:_**

```bash
python Translate_Win_NL.py
```

### Directory Structure:

The script processes files in the given directory and renames them as follows:

.en.srt files will be renamed to .nld.srt after translation.
.srt files will be renamed to .nld.srt after translation.

<br>

## Example Use Case

Place all the .en.srt and .srt subtitle files you want to translate in the same folder.
Run the script and provide the source directory.

The script will:
Process each file in chunks.
Translate the text content from English to Dutch.
Clean up the timestamps.
Save the new file with the .nld.srt extension in the same folder.
<br>

**_Example Input:_**

```plaintext
1
00:00:01,202 --> 00:00:02,436
CLAIRE: Previously on The Good Doctor...

2
00:00:02,570 --> 00:00:04,538
You don't want me to do anything.
Output: The.Good.Doctor.S04E01.1080p.WEBRip.x265-RARBG.nld.srt
```

**_Example Output:_**

```plaintext
1
00:00:01,202 --> 00:00:02,436
Claire: Eerder op De Goede Dokter...

2
00:00:02,570 --> 00:00:04,538
Je wilt niet dat ik iets doe.
```
<br>

## Troubleshooting

If you encounter any issues while running the script, ensure that:

The translatepy library is installed.
You have the necessary permissions to read and write to the specified directories.
If running on Windows, make sure your terminal or IDE supports UTF-8 encoding.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


