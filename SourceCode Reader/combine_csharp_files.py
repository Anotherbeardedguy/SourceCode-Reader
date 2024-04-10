import os
import argparse

def combine_csharp_files(source_folder, output_file):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.cs'):
                    file_path = os.path.join(root, file)
                    outfile.write(f"// Path: {file_path}\n")
                    outfile.write("// Opening file\n")
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read() + "\n")
                    outfile.write("// Closing file\n\n")
    print(f"All C# files have been combined into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine all C# files into one.")
    parser.add_argument("source_folder", type=str, help="The folder where your C# files are located.")
    parser.add_argument("output_file", type=str, help="The output file to write combined C# files.")
    args = parser.parse_args()
    combine_csharp_files(args.source_folder, args.output_file)
