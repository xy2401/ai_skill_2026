import os
import json
import re
from pathlib import Path

def generate_exam_data():
    """
    Generates a structured JSON file containing exam metadata and assets listing.
    """
    res_path = Path("res")
    exam_dir = res_path / "人工智能训练师三级考试平台模拟界面"
    assets_dir = res_path / "人工智能训练师三级上网素材"
    output_file = res_path / "exam_data.json"

    data = {
        "Exam": [],
        "Assets": {}
    }

    # 1. Read Exam Files
    if exam_dir.exists():
        print(f"Reading exam files from: {exam_dir}")
        # Find all .html files in the exam directory
        for html_file in sorted(exam_dir.glob("*.html")):
            try:
                content = html_file.read_text(encoding="utf-8")
                # Extract title using regex
                title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
                title = title_match.group(1).strip() if title_match else html_file.stem
                
                data["Exam"].append({
                    "id": html_file.stem,
                    "title": title,
                    "path": html_file.name
                })
            except Exception as e:
                print(f"Error reading {html_file.name}: {e}")
    else:
        print(f"Warning: Exam directory {exam_dir} not found.")

    # 2. Read Assets Directory
    if assets_dir.exists():
        print(f"Reading asset subdirectories from: {assets_dir}")
        # Iterate through subdirectories
        for subdir in sorted(assets_dir.iterdir()):
            if subdir.is_dir():
                # List all files (excluding directories) in the subdirectory
                file_list = [f.name for f in sorted(subdir.iterdir()) if f.is_file()]
                data["Assets"][subdir.name] = file_list
    else:
        print(f"Warning: Assets directory {assets_dir} not found.")

    # 3. Save to JSON
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Successfully generated: {output_file}")
    except Exception as e:
        print(f"Failed to save JSON: {e}")

if __name__ == "__main__":
    generate_exam_data()
