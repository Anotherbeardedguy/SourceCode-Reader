
import os

def combine_csharp_files_with_tags(source_folder, output_file):
    with open(output_file, 'w') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                # Check if the file is a C# file
                if file.endswith('.cs'):
                    file_path = os.path.join(root, file)
                    # Write the file path and name, and opening tag
                    outfile.write(f"// Path: {file_path}\n")
                    outfile.write("// Opening file\n")
                    with open(file_path, 'r') as infile:
                        # Write the contents of the C# file to the output file
                        outfile.write(infile.read() + "\n")
                    # Write the closing tag
                    outfile.write("// Closing file\n\n")
    print(f"All C# files have been combined into {output_file}")

# Example usage
source_folder = '\Assets\Scripts'
output_file = 'combined_files_with_tags.txt'
combine_csharp_files_with_tags(source_folder, output_file)
