import streamlit as st

st.title("Web Parser")

if "msg" not in st.session_state:
    st.session_state["msg"] = ""

def update_msg():
    st.session_state.msg = msg

data = st.file_uploader(
    label="upload .csv file",
    type="csv",
    disabled=True
    )

msg = st.text_input(
    label="type here...",
    key="text",
    on_change=update_msg,
    )

demo = st.write(
    st.session_state
)

st.write(
    st.session_state.text
)