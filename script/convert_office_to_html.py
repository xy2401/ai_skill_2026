import os
import mammoth
import pandas as pd
from pathlib import Path

def convert_docx_to_html(docx_path, output_path):
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html_body = result.value
        html_content = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

def convert_xlsx_to_html(xlsx_path, output_path):
    df = pd.read_excel(xlsx_path, sheet_name=None)
    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write("<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>")
        for sheet_name, sheet_df in df.items():
            html_file.write(f"<h2>Sheet: {sheet_name}</h2>")
            html_file.write(sheet_df.to_html())
        html_file.write("</body></html>")

def process_directory(directory_path):
    path = Path(directory_path)
    for file_path in path.rglob("*"):
        if file_path.suffix.lower() == ".docx":
            output_path = file_path.with_name(f"{file_path.name}.html")
            print(f"Converting {file_path} to {output_path}")
            convert_docx_to_html(file_path, output_path)
        elif file_path.suffix.lower() in [".xlsx", ".xls"]:
            output_path = file_path.with_name(f"{file_path.name}.html")
            print(f"Converting {file_path} to {output_path}")
            convert_xlsx_to_html(file_path, output_path)

if __name__ == "__main__":
    target_dir = "res/人工智能训练师三级上网素材"
    if os.path.exists(target_dir):
        process_directory(target_dir)
    else:
        print(f"Directory {target_dir} does not exist.")
