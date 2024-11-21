import os
from pathlib import Path
import translatepy
import shutil
import re
import time  # For pausing between chunks

# Regular expression to match subtitle blocks (timestamps and text)
subtitle_block_pattern = re.compile(r'(\d+)\s*(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{3}:\d{3},\d{3})\s*(.*)')

# Function to clean up timestamps (remove extra spaces)
def clean_timestamps(text):
    # Correct the timestamps to remove unnecessary spaces

    # Remove spaces after the colon in timestamps
    cleaned_text = re.sub(r'(\d{2}):\s*(\d{2}):\s*(\d{2}),(\d{3})', r'\1:\2:\3,\4', text)
    
    # Remove spaces around the arrow --> in the timestamps
    cleaned_text = re.sub(r'\s*->\s*', ' --> ', cleaned_text)
    
    return cleaned_text

# Function to perform translation
def translate_text(text, target_lang='nl'):
    try:
        # Using translatepy to translate the entire subtitle block
        translator = translatepy.Translator()
        translated_text = translator.translate(text, target_lang)
        print(f"Translation result: {translated_text.result[:50]}...")  # Debug: print part of the result
        if translated_text.result:
            return translated_text.result
        else:
            print(f"Warning: No translation found for text: {text[:30]}...")
            return ""  # Return an empty string if no translation is found
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""

# Function to process and translate subtitle chunks
def process_chunk(file_path, chunk_start, chunk_size=100):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(f"Processing subtitle file: {file_path}")
    print(f"Total number of lines: {len(lines)}")

    subtitle_block = ""
    chunk_end = chunk_start + chunk_size

    # Read the chunk of subtitle lines (chunk_start to chunk_end)
    for i in range(chunk_start, min(chunk_end, len(lines))):
        line = lines[i].strip()
        print(f"Processing line {i+1}: {line}")  # Debugging: Print each line
        
        match = subtitle_block_pattern.match(line)
        if match:
            subtitle_block += f"{match.group(1)}\n{match.group(2)} --> {match.group(3)}\n{match.group(4)}\n\n"
        else:
            subtitle_block += f"{line}\n"  # Include non-matching lines as well

    # Print the subtitle block for debugging
    if subtitle_block.strip():
        print(f"\nChunk starting at line {chunk_start + 1}:\n{subtitle_block}")
        time.sleep(0.4)  # Pause for 2 seconds to inspect the chunk

        # Translate the subtitle block
        translated_block = translate_text(subtitle_block)
        
        # Write the translated block to the output file
        if translated_block:
            output_file = "/tmp/SRT_Translate/test.srt"
            os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Create directory if it doesn't exist
            with open(output_file, 'a') as out_file:
                out_file.write(f"{translated_block}\n")
            print(f"Translated subtitle written to {output_file}")
        else:
            print("No translation was returned.")

# Function to clean up timestamps in the entire translated file
def clean_translated_file(output_file):
    with open(output_file, 'r') as file:
        content = file.read()

    # Clean the timestamps in the translated text
    cleaned_content = clean_timestamps(content)

    # Write the cleaned content back to the file
    with open(output_file, 'w') as file:
        file.write(cleaned_content)
    print(f"Cleaned the timestamps in the translated file: {output_file}")

# Function to copy the translated file, rename it, and clear test.srt
def copy_and_rename(output_file, source_directory, original_file):
    # Extract the original filename from the source file (without the directory path)
    original_filename = os.path.basename(original_file)

    # Construct the new filename by replacing 'en.srt' with 'nld.srt'
    new_filename = original_filename.replace('.en.srt', '.nld.srt')  # We are renaming test.srt to nld.srt
    
    # Define the full path to copy the file to
    new_file_path = os.path.join(source_directory, new_filename)

    # Copy the file to the source directory with the new name
    shutil.copy(output_file, new_file_path)
    print(f"Copied and renamed file to: {new_file_path}")
    
    # Clear the original test.srt file
    with open(output_file, 'w') as file:
        file.truncate(0)
    print(f"Cleared the content of {output_file}")

# Main function to process all .en.srt files in the directory
def main():
    source_directory = input("Enter the source directory: ")

    # Check if source directory exists
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    # Loop through all .srt files in the directory
    for file_path in Path(source_directory).rglob("*"):
        if str(file_path).endswith(".en.srt"):  # Process only .en.srt files
            # Open the file and read lines to calculate total lines
            with open(file_path, 'r') as file:
                lines = file.readlines()
            total_lines = len(lines)  # Get total number of lines in the file

            chunk_start = 0  # Start at the first chunk (lines 1-100)
            while chunk_start < total_lines:  # Continue until the last line
                process_chunk(str(file_path), chunk_start)
                chunk_start += 100  # Increment to process the next 100 lines

            # After processing all chunks, clean the timestamps in the output file
            output_file = "/tmp/SRT_Translate/test.srt"
            clean_translated_file(output_file)
            
            # Copy and rename the file, then clear the original test.srt file
            copy_and_rename(output_file, source_directory, str(file_path))  # Pass the original file path here

if __name__ == "__main__":
    main()
