# C# File Combiner and Separator

## Description

This project contains two Python scripts designed to work with C# files. The first script combines multiple C# files from a directory into a single text file, including the file path and custom tags. The second script does the reverse, taking a specially formatted text file and recreating the original C# files in their directories.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/Anotherbeardedguy/SourceCode-Reader.git
cd SourceCode-Reader
```
## Usage
### Combining C# Files

To combine all C# files in a directory into a single text file, run:

```bash

python combine_csharp_files.py path/to/your/csharp/files combined_files.txt
```
### Separating C# Files

To separate a combined text file back into its original C# files, run:

```bash

python separate_csharp_files.py combined_files_with_tags.txt path/to/target/directory
```
## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
