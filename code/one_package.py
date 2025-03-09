'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

st.title('Package Processing')

package = st.text_input('Enter package data: ')

if package:
    parsed_package = packaging.parse_packaging(package)
    
    total = packaging.calc_total_units(parsed_package)
    unit = packaging.get_unit(parsed_package)
    
    st.text(f"Parsed package: {parsed_package}")
    
    for item in parsed_package:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f'{name} ➡️ {size}')
    
    st.success(f'Total Package Size: {total} {unit}')