import os
import argparse

def recreate_files_from_text(input_file, root_folder):
    file_content = []
    current_path = ""
    reading_file = False

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recreate C# files from a combined text file.")
    parser.add_argument("input_file", type=str, help="The combined text file to process.")
    parser.add_argument("root_folder", type=str, help="The root folder to recreate C# files in.")
    args = parser.parse_args()
    recreate_files_from_text(args.input_file, args.root_folder)
