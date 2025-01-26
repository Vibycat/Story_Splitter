import os

# File path and settings
INPUT_FOLDER = r"D:\Content_Creation\Full_Stories"  # Path to your input directory containing text files
OUTPUT_FOLDER = "Text_Files"  # Folder to save the trimmed text files
CHAR_LIMIT = 1800  # Adjusted character limit per section to match your updated threshold

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def split_text_file(input_file, char_limit, title, output_folder):
    """
    Reads a text file, divides it into sections of a specified character limit,
    and saves each section to a new file with a user-provided title and proper formatting.
    """
    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    total_characters = len(content)
    print(f"Processing file: {input_file}")
    print(f"Total characters in file: {total_characters}")

    # Split content into sections of approximately `char_limit` characters
    sections = [content[i:i + char_limit] for i in range(0, total_characters, char_limit)]

    # Save each section to a separate file with filenames like "{title}_Part1.txt"
    for idx, section in enumerate(sections, start=1):
        output_file = os.path.join(output_folder, f"{title}_Part{idx}.txt")
        with open(output_file, "w", encoding="utf-8") as output:
            output.write(section)
        print(f"Saved {output_file} with {len(section)} characters.")

    print(f"Finished processing: {input_file}. Total sections created: {len(sections)}\n")

# Main function to process all text files in the input folder
def process_all_files(input_folder, char_limit, output_folder):
    """
    Processes all `.txt` files in the input folder with user-provided title.
    """
    # Ask the user for a title
    title = input("Enter a base title for the output files: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return

    # Loop through all `.txt` files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):  # Process only text files
            input_file_path = os.path.join(input_folder, file_name)
            split_text_file(input_file_path, char_limit, title, output_folder)

# Call the function to process all files
process_all_files(INPUT_FOLDER, CHAR_LIMIT, OUTPUT_FOLDER)
