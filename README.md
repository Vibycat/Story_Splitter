# README: Text File Splitter Script

## Overview
This Python script processes text files from a specified input directory, divides the content into equal parts based on a character limit, and saves the sections as new text files in an output directory. Each section is saved with a user-defined title and numbered parts.

---

## Features
1. **Processes All `.txt` Files**: Automatically scans the input directory and processes all `.txt` files.
2. **Customizable Character Limit**: Splits text files into sections based on a user-defined character limit.
3. **User-Defined Titles**: Allows you to provide a base title for the output files.
4. **Formatted Output Filenames**: Saves files in the format: `{title}_Part1.txt`, `{title}_Part2.txt`, etc.
5. **Output Folder Management**: Ensures that all processed files are saved in a specified output folder.

---

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

---

## File and Folder Structure
- **Input Folder**: Place your `.txt` files in the specified input directory.
- **Output Folder**: Processed files will be saved in the `Text_Files` folder by default.

---

## Script Settings
### Input Variables
- `INPUT_FOLDER`: Path to the directory containing `.txt` files to be processed.
- `OUTPUT_FOLDER`: Path to the directory where the processed files will be saved.
- `CHAR_LIMIT`: Maximum number of characters (including spaces and punctuation) per output section.

---

## How to Use the Script
### Step 1: Configure Settings
1. Update the `INPUT_FOLDER` variable with the path to your input directory.
2. (Optional) Update the `OUTPUT_FOLDER` variable to change the output directory.
3. Set the `CHAR_LIMIT` variable to define the character limit per section.

### Step 2: Run the Script
1. Open a terminal or command prompt.
2. Run the script using the command:
   ```bash
   python script_name.py
   ```
3. Enter the base title for the output files when prompted.

### Step 3: Check Output
Processed files will be saved in the output folder with filenames like:
```
{title}_Part1.txt
{title}_Part2.txt
...
```

---

## Example
### Input:
- **File**: `story.txt`
- **Content**: 5000 characters

### Script Settings:
- `CHAR_LIMIT`: 1800
- Title: `MyStory`

### Output:
```
Text_Files/MyStory_Part1.txt (1800 characters)
Text_Files/MyStory_Part2.txt (1800 characters)
Text_Files/MyStory_Part3.txt (remaining characters)
```

---

## Troubleshooting
- **Error: "Title cannot be empty."**
  Ensure you provide a valid title when prompted.

- **File Not Processed**:
  Ensure the input folder contains `.txt` files and that the path is correctly set in `INPUT_FOLDER`.

- **Output Files Overwritten**:
  The script overwrites existing files with the same name in the output folder. Ensure unique titles for each run.

---

## Customization
1. **Change Output File Format**:
   Modify the output filename logic in the script:
   ```python
   output_file = os.path.join(output_folder, f"{title}_Part{idx}.txt")
   ```
2. **Adjust Character Limit**:
   Update the `CHAR_LIMIT` variable in the script to your preferred value.

---

## License
This script is free to use and distribute. Modify it as needed for your projects.
