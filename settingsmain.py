import streamlit as st

def settings():
    APIkey = st.text_input("Your API-Key")
    
    st.session_state["API-key"] = APIkey