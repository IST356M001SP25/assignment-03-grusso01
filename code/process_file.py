'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Package File Processor")

uploaded_file = st.file_uploader("Upload a package file:")

if uploaded_file:
    out_filename = uploaded_file.name.replace(".txt", ".json")
    package_list = []
    
    text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    
    for package_line in text.split("\n"):
        if not package_line.strip():
            continue
            
        package_data = packaging.parse_packaging(package_line.strip())
        package_size = packaging.calc_total_units(package_data)
        unit_type = packaging.get_unit(package_data)
        
        package_list.append(package_data)
        st.info(f"{package_line.strip()} ➡️ Total 📦 Size: {package_size} {unit_type}")
    
    if package_list:
        with open(f"./data/{out_filename}", "w") as output_file:
            json.dump(package_list, output_file, indent=4)
        
        st.success(f"{len(package_list)} packages written to {out_filename}", icon="💾")