'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title('Processing for Package Files')


if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0


file = st.file_uploader('Upload package file: ')


if file:
    filename = file.name
    json_filename = filename.replace('.txt', '.json')
    packages = []
    text = StringIO(file.getvalue().decode('utf-8')).read()
    for line in text.split('\n'):
        line = line.strip()
        pkg = packaging.parse_packaging(line)
        total = packaging.calc_total_units(pkg)
        unit = packaging.get_unit(pkg)
        packages.append(pkg)
        st.info(f'{line} ➡️ Total 📦 Size: {total} {unit}')
    count = len(packages)
    with open(f'./data/{json_filename}', 'w') as f:
        json.dump(packages, f, indent=4)
    summary = f'{count} packages written to {json_filename}'

    st.session_state.summaries.append(summary)
    st.session_state.total_files += 1
    st.session_state.total_lines += count

    for s in st.session_state.summaries:
        st.info(s, icon='💾')
    st.success(f'{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed')