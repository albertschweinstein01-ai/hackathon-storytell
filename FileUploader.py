import streamlit as st
import pandas as pd
from io import StringIO

def on_upper_clicked():
    st.experimental_rerun


def fileupload(i):

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        st.session_state["File_uploaded"] = True
        
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        return string_data
    

