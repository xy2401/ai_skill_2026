import os
import json
import difflib
from pathlib import Path

def extract_code_from_ipynb(ipynb_path, py_path):
    """提取 ipynb 中的代码单元格到 .py 文件"""
    try:
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        code_cells = []
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                # 拼接单元格中的代码行，并确保末尾有换行符
                code = "".join(cell.get('source', []))
                if code and not code.endswith('\n'):
                    code += '\n'
                code_cells.append(code)
        
        # 用两行空行分隔不同的单元格
        full_code = "\n\n".join(code_cells)
        
        with open(py_path, 'w', encoding='utf-8') as f:
            f.write(full_code)
        
        # print(f"已导出: {py_path}")
        return True
    except Exception as e:
        print(f"转换 {ipynb_path} 时出错: {e}")
        return False

def diff_files(file1, file2):
    """比较两个文件的差异并保存到 .diff 文件"""
    try:
        with open(file1, 'r', encoding='utf-8') as f1, \
             open(file2, 'r', encoding='utf-8') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
        diff = difflib.unified_diff(
            lines1, lines2, 
            fromfile=str(file1), tofile=str(file2),
            n=0,
            lineterm=''
        )
        
        diff_text = list(diff)
        if diff_text:
            diff_file_path = file1.parent / (file1.name + ".diff")
            with open(diff_file_path, 'w', encoding='utf-8') as df:
                df.writelines(line + '\n' for line in diff_text)
            
            print(f"发现差异并已保存: {diff_file_path}")
            return True
        return False
    except Exception as e:
        print(f"对比 {file1} 和 {file2} 时出错: {e}")
        return False

def main():
    base_dir = Path("res/人工智能训练师三级上网素材")
    if not base_dir.exists():
        print(f"错误: 目录 {base_dir} 不存在")
        return

    # 第一阶段：提取所有 .ipynb 文件
    ipynb_files = list(base_dir.rglob("*.ipynb"))
    for ipynb_path in ipynb_files:
        # 跳过 checkpoints
        if ".ipynb_checkpoints" in str(ipynb_path):
            continue
            
        py_path = ipynb_path.with_suffix(".ipynb.py")
        extract_code_from_ipynb(ipynb_path, py_path)

    # 第二阶段：对比 .ipynb.py 和 .ans.ipynb.py
    for py_path in base_dir.rglob("*.ipynb.py"):
        # 检查是否是对应的 ans 版本
        if py_path.name.endswith(".ans.ipynb.py"):
            continue
        
        # 构造对应的 .ans.ipynb.py 路径
        # 假设 1.1.1.ipynb 对应 1.1.1.ans.ipynb
        # 这里的命名逻辑是 1.1.1.ipynb -> 1.1.1.ipynb.py
        # 1.1.1.ans.ipynb -> 1.1.1.ans.ipynb.py
        # 所以我们查找同目录下是否有 .ans.ipynb.py
        ans_py_name = py_path.name.replace(".ipynb.py", ".ans.ipynb.py")
        ans_py_path = py_path.parent / ans_py_name
        
        if ans_py_path.exists():
            diff_files(py_path, ans_py_path)

if __name__ == "__main__":
    main()
