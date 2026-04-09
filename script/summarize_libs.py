import os
import re
from pathlib import Path
from collections import defaultdict

def extract_code_from_html(html_path):
    """
    Extracts Python code from the Jupyter-exported HTML file.
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all highlight blocks
    # Structure: <div class="highlight hl-ipython3"><pre><span></span>...code...</pre></div>
    # Note: The actual code might have many <span> tags for syntax highlighting.
    # We need to strip those <span> tags.
    
    code_blocks = []
    # Find the content between <pre><span></span> and </pre>
    matches = re.findall(r'<div class="highlight hl-ipython3"><pre><span></span>(.*?)</pre>', content, re.DOTALL)
    
    for match in matches:
        # Strip all HTML tags from the match to get pure code
        clean_code = re.sub(r'<[^>]+>', '', match)
        # Unescape HTML entities if any (like &gt;, &lt;, &amp;)
        import html
        clean_code = html.unescape(clean_code)
        code_blocks.append(clean_code)
        
    return "\n".join(code_blocks)

def analyze_code(code):
    """
    Extracts used libraries and functions/methods from the code.
    """
    libraries = set()
    functions = defaultdict(set)
    
    # 1. Find imports
    # import pandas as pd -> pd
    # import numpy as np -> np
    # from sklearn.model_selection import train_test_split -> sklearn.model_selection, train_test_split
    
    import_map = {} # alias -> full_name or module
    
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        # import pandas as pd
        m1 = re.match(r'^import\s+([\w\.]+)(?:\s+as\s+(\w+))?', line)
        if m1:
            full_name = m1.group(1)
            alias = m1.group(2) if m1.group(2) else full_name
            import_map[alias] = full_name
            libraries.add(full_name)
            continue
            
        # from sklearn.linear_model import LogisticRegression
        m2 = re.match(r'^from\s+([\w\.]+)\s+import\s+([\w\s,]+)', line)
        if m2:
            module = m2.group(1)
            funcs = [f.strip() for f in m2.group(2).split(',')]
            libraries.add(module)
            for f in funcs:
                functions[module].add(f)
                import_map[f] = f"{module}.{f}"
    
    # 2. Find function calls and methods
    # pattern: something.func(
    # pattern: func(
    
    # Common built-in functions to ignore or group
    builtins = {'print', 'len', 'range', 'int', 'float', 'str', 'list', 'dict', 'set', 'sum', 'min', 'max'}
    
    # Find calls like obj.method(
    method_calls = re.findall(r'(\w+)\.([\w\d_]+)\(', code)
    for obj, method in method_calls:
        if obj in import_map:
            lib = import_map[obj]
            functions[lib].add(method)
        else:
            # Might be a dataframe or numpy array method
            # We'll group these under "Pandas/Numpy Methods" if we can't tell
            # For simplicity, if we see .read_csv it's likely pandas if 'pd' was imported
            pass

    # Specific common patterns in this dataset
    # pd.read_csv, pd.cut, np.where, np.inf, data.groupby, etc.
    if 'pd' in import_map:
        for m in re.findall(r'pd\.([\w\d_]+)', code):
            functions['pandas'].add(m)
    if 'np' in import_map:
        for m in re.findall(r'np\.([\w\d_]+)', code):
            functions['numpy'].add(m)
    if 'plt' in import_map:
        for m in re.findall(r'plt\.([\w\d_]+)', code):
            functions['matplotlib.pyplot'].add(m)
    if 'sns' in import_map:
        for m in re.findall(r'sns\.([\w\d_]+)', code):
            functions['seaborn'].add(m)

    # DataFrame methods (best effort)
    df_methods = {'value_counts', 'groupby', 'apply', 'dropna', 'fillna', 'mean', 'sum', 'count', 'reset_index', 'rename', 'merge', 'concat', 'sort_values', 'head', 'describe', 'info'}
    for method in df_methods:
        if re.search(rf'\.({method})\(', code):
            functions['pandas (DataFrame methods)'].add(method)

    # Scikit-learn common methods
    sklearn_methods = {'fit', 'predict', 'score', 'fit_transform', 'transform'}
    for method in sklearn_methods:
        if re.search(rf'\.({method})\(', code):
            functions['sklearn (common methods)'].add(method)

    return libraries, functions

def main():
    source_dir = Path("欣旋/二十题代码答案及运行")
    all_libraries = set()
    all_functions = defaultdict(set)
    
    if not source_dir.exists():
        print(f"Directory {source_dir} not found.")
        return

    html_files = sorted(list(source_dir.glob("*.html")))
    print(f"Analyzing {len(html_files)} files...")

    for html_file in html_files:
        code = extract_code_from_html(html_file)
        libs, funcs = analyze_code(code)
        all_libraries.update(libs)
        for lib, fset in funcs.items():
            all_functions[lib].update(fset)

    # Generate lib.md
    with open("lib.md", "w", encoding="utf-8") as f:
        f.write("# 二十题代码中使用到的类库和函数汇总\n\n")
        
        # Sort libraries
        sorted_libs = sorted(all_functions.keys())
        
        for lib in sorted_libs:
            f.write(f"### {lib}\n")
            sorted_funcs = sorted(list(all_functions[lib]))
            for func in sorted_funcs:
                f.write(f"- `{func}`\n")
            f.write("\n")

    print("Done. Results saved to lib.md")

if __name__ == "__main__":
    main()
