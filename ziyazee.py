import streamlit as st
st.title("Interactive streamlit app")
name=st.text_input("Enter your first name")
name1=st.text_input("Enter your last name")
if st.button("submit"):
    st.write(f"Hello,{name,name1}!Welcome to streamlit.")

