import streamlit as st

def writeandprompt():

    if st.session_state["File_uploaded"] is True:
        st.header("Your text")

    else:
        st.header("Your text")
        st.session_state["story_string"] = " "

    st.text_area("literary masterpiece",st.session_state["story_string"], height=500, placeholder="Write your story here", key="text")    
    st.text_area(" ", height=200, placeholder="Prompt Claude for ideas") 