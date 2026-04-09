import json
from pathlib import Path

def generate_exam_markdown():
    """
    Reads exam_data.json and generates exam_data.md in the same directory (res/).
    """
    res_path = Path("res")
    json_file = res_path / "exam_data.json"
    output_md = res_path / "exam_data.md"

    if not json_file.exists():
        print(f"Error: {json_file} not found. Please run the generation script first.")
        return

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    md_content = ["# 人工智能训练师三级考试试题汇总\n"]
    
    # 1. Generate Table of Contents (TOC)
    md_content.append("## 目录")
    for item in data.get("Exam", []):
        title = item["title"]
        # Create a simple anchor link. Note: Most MD viewers use lowercase and hyphens for anchors.
        # But just linking to the name works in many environments.
        anchor = title.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(".", "")
        md_content.append(f"- [{title}](#{anchor})")
    
    md_content.append("\n---\n")

    # Base paths for links (relative to res/ directory where the .md file will live)
    exam_base = "./人工智能训练师三级考试平台模拟界面"
    assets_base = "./人工智能训练师三级上网素材"
    
    # AI Analysis paths (relative to res/ directory)
    AI_ANALYSIS_CONFIG = {
        "gemini": "../study/gemini/",
        #"codex": "../study/codex/",
    }

    for item in data.get("Exam", []):
        exam_id = item["id"]
        title = item["title"]
        exam_html_name = item["path"]
        
        # 2. Detailed Content Section
        md_content.append(f"## {title}")
        
        # 1. 进入模拟考场
        md_content.append(f"- **[进入模拟考场]({exam_base}/{exam_html_name})**")
        
        # Get Assets Breakdown
        assets = data.get("Assets", {}).get(exam_id, [])
        ques_ipynb = [f for f in assets if "ipynb" in f.lower() and ".ans." not in f.lower()]
        ans_ipynb = [f for f in assets if ".ans." in f.lower()]
        other_assets = [f for f in assets if "ipynb" not in f.lower()]

        # 2. 相关素材
        if other_assets:
            md_content.append("- **相关素材**:")
            for f in other_assets:
                md_content.append(f"  - [{f}]({assets_base}/{exam_id}/{f})")

        # 3. 题目代码
        if ques_ipynb:
            md_content.append("- **题目代码**:")
            for f in ques_ipynb:
                md_content.append(f"  - [{f}]({assets_base}/{exam_id}/{f})")

        # 4. 参考解答
        if ans_ipynb:
            md_content.append("- **参考解答**:")
            for f in ans_ipynb:
                md_content.append(f"  - [{f}]({assets_base}/{exam_id}/{f})")

        # 5. AI 解析 (One per line as a sub-list)
        md_content.append("- **AI 解析**:")
        for name, base_path in AI_ANALYSIS_CONFIG.items():
            md_content.append(f"  - [{name}]({base_path}{exam_id}.md)")
        
        md_content.append("\n---\n")

    try:
        with open(output_md, "w", encoding="utf-8") as f:
            f.write("\n".join(md_content))
        print(f"Successfully generated: {output_md}")
    except Exception as e:
        print(f"Failed to save Markdown: {e}")

if __name__ == "__main__":
    generate_exam_markdown()
