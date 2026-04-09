import json
import os
from pathlib import Path

def create_notebook(lib_name, methods):
    """
    Creates a Jupyter Notebook structure for a given library and its methods.
    """
    cells = []
    
    # Base name for import (e.g., 'pandas' from 'pandas (DataFrame methods)')
    clean_lib = lib_name.split(' ')[0]
    
    # 1. Import cell
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [f"import {clean_lib}\n", f"print(f'{clean_lib} version: {{{clean_lib}.__version__ if hasattr({clean_lib}, \"__version__\") else \"N/A\"}}')"]
    })

    # 2. Help library
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [f"help({clean_lib})"]
    })

    # 3. Dir library
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [f"dir({clean_lib})"]
    })

    # 4. Help for each method
    for method in methods:
        # Handle special cases like 'pandas (DataFrame methods)'
        if 'DataFrame methods' in lib_name:
            source = f"help(pandas.DataFrame.{method})"
        elif 'sklearn (common methods)' in lib_name:
            # sklearn common methods are usually on an instance, but we can't easily help() 
            # without an instance. We'll skip or use a generic one if possible.
            continue
        elif '.' in lib_name:
            # Submodules like sklearn.metrics
            source = f"help({lib_name}.{method})"
        else:
            source = f"help({clean_lib}.{method})"
            
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"### Help for `{method}`"]
        })
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [source]
        })

    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    return nb

def main():
    lib_md_path = Path("lib.md")
    output_dir = Path("study/lib")
    output_dir.mkdir(parents=True, exist_ok=True)

    if not lib_md_path.exists():
        print("lib.md not found.")
        return

    with open(lib_md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_lib = None
    libs_data = {}

    for line in lines:
        line = line.strip()
        if line.startswith("### "):
            current_lib = line.replace("### ", "")
            libs_data[current_lib] = []
        elif line.startswith("- `") and current_lib:
            method = line.replace("- `", "").replace("`", "")
            libs_data[current_lib].append(method)

    for lib, methods in libs_data.items():
        # Sanitize filename
        filename = lib.replace(" ", "_").replace("(", "").replace(")", "").lower() + ".ipynb"
        nb_content = create_notebook(lib, methods)
        
        with open(output_dir / filename, "w", encoding="utf-8") as f:
            json.dump(nb_content, f, ensure_ascii=False, indent=1)
        print(f"Created: {filename}")

if __name__ == "__main__":
    main()
