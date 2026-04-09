import os
import argparse
from markitdown import MarkItDown
from pathlib import Path

def convert_to_md(source_dir, extensions, output_dir=None):
    """
    Converts files with specific extensions in a directory to Markdown using MarkItDown.
    """
    md = MarkItDown()
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # If output_dir is not provided, use the source directory
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = source_path

    # Normalize extensions (e.g., '.docx' instead of 'docx')
    exts = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
    
    print(f"Searching for files with extensions {exts} in '{source_dir}'...")

    files_found = 0
    files_converted = 0

    # Iterate through files in the directory
    for file in source_path.iterdir():
        if file.is_file() and file.suffix.lower() in exts:
            files_found += 1
            print(f"Converting: {file.name} ...", end=" ", flush=True)
            
            try:
                # Perform the conversion
                result = md.convert(str(file))
                
                # Define output filename
                md_filename = file.stem + ".md"
                target_file = output_path / md_filename
                
                # Save the Markdown content
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                
                print("Done.")
                files_converted += 1
            except Exception as e:
                print(f"Failed! Error: {e}")

    print("-" * 30)
    print(f"Found {files_found} files, successfully converted {files_converted}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert files to Markdown using Microsoft MarkItDown.")
    parser.add_argument("dir", help="The source directory to scan for files.")
    parser.add_argument("--ext", nargs="+", default=[".pdf", ".docx", ".xlsx", ".pptx"], 
                        help="File extensions to convert (e.g., .pdf .docx). Default: .pdf .docx .xlsx .pptx")
    parser.add_argument("--output", "-o", help="The output directory (optional).")

    args = parser.parse_args()

    convert_to_md(args.dir, args.ext, args.output)
