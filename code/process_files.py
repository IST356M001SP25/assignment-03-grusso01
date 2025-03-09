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

st.title("Process Package Files")

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0

file = st.file_uploader("Upload a package file:")

def process_file(file):
    json_filename = file.name.replace(".txt", ".json")
    
    file_content = file.getvalue().decode("utf-8")
    lines = file_content.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    packages = []
    for line in non_empty_lines:
        packages.append(packaging.parse_packaging(line))

    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)

    return len(packages), json_filename

if file:
    result = process_file(file)
    count = result[0]
    json_filename = result[1]

    st.session_state.summaries.append(f"{count} packages written to {json_filename}")
    st.session_state.total_files += 1
    st.session_state.total_lines += count

    for summary in st.session_state.summaries:
        st.info(summary, icon="💾")

    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed")
