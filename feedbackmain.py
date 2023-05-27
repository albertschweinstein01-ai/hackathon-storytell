import streamlit as st
import requests



def dosomething():
    #APIcall(text)
    st.write("Claude does not approve of your lack of creative writing")


def buttonandoutput():

    st.session_state["claude_answered"] = False

    col1, col2 = st.columns(2)
    with col1:
        
        if st.session_state["File_uploaded"] is True:
            st.header("Your text and True")

        else:
            st.header("Your text and False")
            st.session_state[""] = " "

        st.text_area("literary masterpiece", st.session_state["story_string"], height=500, placeholder="Write your story here", key="text2") 
    with col2:
        
        button1text = "Ask Claude about your writing style"

        if st.button("Ask Claude about your writing style"):
            dosomething()
        st.button("Ask Claude about ideas to continue your story")
        st.button("Ask Claude about your characters feelings at this moment")

        if "claude_answer" in st.session_state and st.session_state["claude_answered"] == True:
            st.write(st.session_state["claude_answer"])
        


