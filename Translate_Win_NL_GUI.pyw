import os
from pathlib import Path
import translatepy
import shutil
import re
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading  # Import threading module

# Regular expression to match subtitle blocks (timestamps and text)
subtitle_block_pattern = re.compile(r'(\d+)\s*(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\s*(.*)')

# Function to clean up timestamps (remove unnecessary spaces)
def clean_timestamps(text):
    cleaned_text = re.sub(r'(\d{2}):\s*(\d{2}):\s*(\d{2}),(\d{3})', r'\1:\2:\3,\4', text)
    cleaned_text = re.sub(r'\s*->\s*', ' --> ', cleaned_text)
    return cleaned_text

# Function to perform translation
def translate_text(text, target_lang='nl'):
    try:
        translator = translatepy.Translator()
        translated_text = translator.translate(text, target_lang)
        if translated_text.result:
            return translated_text.result
        else:
            print(f"Warning: No translation found for text: {text[:30]}...")
            return ""
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""

# Function to process and translate subtitle chunks
def process_chunk(file_path, chunk_start, chunk_size=100):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    subtitle_block = ""
    chunk_end = chunk_start + chunk_size

    for i in range(chunk_start, min(chunk_end, len(lines))):
        line = lines[i].strip()
        match = subtitle_block_pattern.match(line)
        if match:
            subtitle_block += f"{match.group(1)}\n{match.group(2)} --> {match.group(3)}\n{match.group(4)}\n\n"
        else:
            subtitle_block += f"{line}\n"

    translated_block = translate_text(subtitle_block)
    return translated_block

# Function to process all .en.srt files in the directory
def process_files(source_directory, progress_callback):
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    for file_path in Path(source_directory).rglob("*"):
        if str(file_path).endswith(".en.srt"):
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            total_lines = len(lines)

            chunk_start = 0
            translated_chunks = []

            while chunk_start < total_lines:
                translated_block = process_chunk(str(file_path), chunk_start)
                translated_chunks.append(translated_block)
                chunk_start += 100

                # Update the progress bar
                progress = (chunk_start / total_lines) * 100
                progress_callback(progress)

            output_file = "/tmp/SRT_Translate/test.srt"
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            with open(output_file, 'a', encoding='utf-8') as out_file:
                for chunk in translated_chunks:
                    out_file.write(f"{chunk}\n")

            clean_translated_file(output_file)
            copy_and_rename(output_file, source_directory, str(file_path))

    messagebox.showinfo("Translation Complete", "All subtitle files have been translated successfully.")

# Function to clean up timestamps in the entire translated file
def clean_translated_file(output_file):
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = clean_timestamps(content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
    print(f"Cleaned the timestamps in the translated file: {output_file}")

# Function to copy the translated file, rename it, and clear test.srt
def copy_and_rename(output_file, source_directory, original_file):
    original_filename = os.path.basename(original_file)
    new_filename = original_filename.replace('.en.srt', '.nld.srt')

    new_file_path = os.path.join(source_directory, new_filename)

    shutil.copy(output_file, new_file_path)
    print(f"Copied and renamed file to: {new_file_path}")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.truncate(0)
    print(f"Cleared the content of {output_file}")

# Function to select source directory using a GUI
def select_directory():
    source_directory = filedialog.askdirectory()
    if source_directory:
        # Start the file processing in a separate thread
        threading.Thread(target=process_files, args=(source_directory, update_progress), daemon=True).start()
    else:
        messagebox.showwarning("Warning", "No directory selected")

# Function to update the progress bar
def update_progress(progress):
    progress_var.set(progress)
    root.update_idletasks()

# Main function to create the GUI
def main():
    global progress_var, root

    root = tk.Tk()
    root.title("Subtitle SRT Translator - English to Dutch")
    root.geometry("450x150")

    select_button = tk.Button(root, text="Select Source Directory", command=select_directory)
    select_button.pack(pady=20)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(pady=20, fill=tk.X, padx=20)

    root.mainloop()

if __name__ == "__main__":
    main()
