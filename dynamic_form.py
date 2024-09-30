import streamlit as st
import json

def create_form(form_elements):
    form_data = {}
    for element in form_elements:
        element_type = element['type']
        element_label = element['label']
        element_key = element['key']
        
        if element_type == 'text':
            form_data[element_key] = st.text_input(element_label)
        elif element_type == 'number':
            form_data[element_key] = st.number_input(element_label)
        elif element_type == 'textarea':
            form_data[element_key] = st.text_area(element_label)
        elif element_type == 'selectbox':
            options = element.get('options', [])
            form_data[element_key] = st.selectbox(element_label, options)
        elif element_type == 'checkbox':
            form_data[element_key] = st.checkbox(element_label)
        elif element_type == 'radio':
            options = element.get('options', [])
            form_data[element_key] = st.radio(element_label, options)
    
    return form_data

st.title("Dynamic Form Generator")
try:
    with open('form.json', 'r') as file:
        form_elements = json.load(file)
    
    form_data = create_form(form_elements)
    
    if st.button('Submit'):
        st.json(form_data)
except FileNotFoundError:
    st.error("The file 'form.json' was not found.")
except json.JSONDecodeError:
    st.error("The file 'form.json' is not a valid JSON file.")