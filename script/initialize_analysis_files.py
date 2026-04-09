import json
import argparse
from pathlib import Path

def initialize_analysis_files(target_dir_name):
    """
    Reads exam_data.json and creates initial Markdown files in the specified study subdirectory.
    """
    res_path = Path("res")
    json_file = res_path / "exam_data.json"
    
    # Target directory (e.g., study/gemini)
    target_dir = Path("study") / target_dir_name

    if not json_file.exists():
        print(f"Error: {json_file} not found. Please run the generation script first.")
        return

    if not target_dir.exists():
        print(f"Creating directory: {target_dir}")
        target_dir.mkdir(parents=True, exist_ok=True)

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    files_created = 0
    files_skipped = 0

    print(f"Initializing files in '{target_dir}'...")

    for item in data.get("Exam", []):
        exam_id = item["id"]
        title = item["title"]
        
        file_path = target_dir / f"{exam_id}.md"

        if file_path.exists():
            print(f"Warning: File already exists, skipping: {file_path}")
            files_skipped += 1
            continue

        try:
            content = f"# {title}\n\n# 解析\n"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created: {file_path.name}")
            files_created += 1
        except Exception as e:
            print(f"Failed to create {file_path.name}: {e}")

    print("-" * 30)
    print(f"Total created: {files_created}")
    print(f"Total skipped (existed): {files_skipped}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize AI analysis Markdown files for each exam item.")
    parser.add_argument("target", help="The subdirectory name under 'study/' (e.g., gemini or codex).")

    args = parser.parse_args()

    initialize_analysis_files(args.target)
