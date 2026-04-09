import argparse
import shutil
from pathlib import Path

def copy_notebooks_for_answers(root_dir):
    """
    Recursively finds all *.ipynb files and creates a copy named *.ans.ipynb.
    """
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' does not exist.")
        return

    print(f"Scanning for Jupyter Notebooks in '{root_path.absolute()}'...")

    files_found = 0
    files_copied = 0
    files_skipped = 0

    # Recursive glob for .ipynb files
    for ipynb_file in root_path.rglob("*.ipynb"):
        # Skip if the file is already an answer file to avoid recursion/duplicates
        if ipynb_file.name.endswith(".ans.ipynb"):
            files_skipped += 1
            continue
        
        files_found += 1
        
        # Define the target filename
        ans_filename = ipynb_file.stem + ".ans.ipynb"
        ans_file_path = ipynb_file.parent / ans_filename
        
        # Check if the answer file already exists
        if ans_file_path.exists():
            print(f"Skipping: {ans_file_path.name} already exists.")
            files_skipped += 1
            continue

        try:
            # Copy the file
            shutil.copy2(ipynb_file, ans_file_path)
            print(f"Copied: {ipynb_file.name} -> {ans_filename}")
            files_copied += 1
        except Exception as e:
            print(f"Failed to copy {ipynb_file.name}: {e}")

    print("-" * 30)
    print(f"Found {files_found} notebooks.")
    print(f"Successfully created {files_copied} answer copies.")
    print(f"Skipped {files_skipped} files (already exist or are answer files).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy *.ipynb files to *.ans.ipynb for answer storage.")
    parser.add_argument("dir", help="The root directory to scan recursively.")

    args = parser.parse_args()

    copy_notebooks_for_answers(args.dir)
