import os

def recreate_files_from_text(input_file):
    file_content = []
    current_path = ""
    reading_file = False
    # Use the current working directory as the root folder
    root_folder = os.getcwd()

    with open(input_file, 'r') as infile:
        for line in infile:
            if line.startswith("// Path:"):
                if current_path and file_content:
                    save_file(os.path.join(root_folder, current_path), file_content)
                    file_content = []
                full_path = line[len("// Path: "):].strip()
                path_parts = full_path.split(os.sep)
                last_folder_name = path_parts[-2] if len(path_parts) > 1 else ""
                file_name = path_parts[-1]
                current_path = os.path.join(last_folder_name, file_name)
            elif line.startswith("// Opening file"):
                reading_file = True
            elif line.startswith("// Closing file"):
                reading_file = False
                save_file(os.path.join(root_folder, current_path), file_content)
                file_content = []
                current_path = ""
            elif reading_file:
                file_content.append(line)

        if current_path and file_content:
            save_file(os.path.join(root_folder, current_path), file_content)

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as outfile:
        outfile.writelines(content)
    print(f"File saved: {path}")

# Example usage
input_file = 'combined_files_with_tags.txt'
recreate_files_from_text(input_file)
