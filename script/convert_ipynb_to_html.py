import argparse
import subprocess
from pathlib import Path

def convert_ipynb_to_html(root_dir):
    """
    Recursively finds all *.ipynb files and converts them to *.ipynb.html using nbconvert.
    """
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' does not exist.")
        return

    print(f"Scanning for Jupyter Notebooks in '{root_path.absolute()}'...")

    files_found = 0
    files_converted = 0

    # Recursive glob for .ipynb files
    for ipynb_file in root_path.rglob("*.ipynb"):
        files_found += 1
        
        # Define the target filename (example: test.ipynb -> test.ipynb.html)
        # Note: nbconvert by default would use test.html, so we manually specify the output
        output_filename = ipynb_file.name + ".html"
        target_file = ipynb_file.parent / output_filename
        
        print(f"Converting: {ipynb_file.name} ...", end=" ", flush=True)

        try:
            # Use jupyter nbconvert to perform the conversion
            # --to html specifies the format
            # --output specifies the name of the output file
            # --output-dir specifies where to save it (same parent as original)
            cmd = [
                "jupyter", "nbconvert", 
                "--to", "html", 
                "--output", output_filename, 
                "--output-dir", str(ipynb_file.parent),
                str(ipynb_file)
            ]
            
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("Done.")
            files_converted += 1
        except subprocess.CalledProcessError as e:
            print(f"Failed! Error: {e.stderr.strip()}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("-" * 30)
    print(f"Found {files_found} notebooks.")
    print(f"Successfully converted {files_converted} to HTML.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert *.ipynb files to *.ipynb.html for easy viewing.")
    parser.add_argument("dir", help="The root directory to scan recursively.")

    args = parser.parse_args()

    convert_ipynb_to_html(args.dir)
