import streamlit as st

st.set_page_config(layout="wide")

from modularcharacterInfo import charactercard
from writingmain import writeandprompt
from feedbackmain import buttonandoutput
from settingsmain import settings
from FileUploader import fileupload, on_upper_clicked

if "File_uploaded" not in st.session_state:
    st.session_state["File_uploaded"] = False

tab1, tab2, tab3 = st.tabs(["Writing", "Feedback","Testing"])

with tab1:
    writeandprompt()

with tab2:
    buttonandoutput()
    
with tab3:
   settings()
   st.session_state["story_string"] = fileupload(0)
   st.write(st.session_state["API-key"])
   st.button("Override current Text", on_click=on_upper_clicked)

with st.sidebar:
   charactercard()



 
