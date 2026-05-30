
import streamlit as st

st.title("AI Cover Letter Generator")

name = st.text_input("Name")
role = st.text_input("Target Role")
skills = st.text_area("Skills")
experience = st.text_area("Experience")

if st.button("Generate Cover Letter"):
    st.success("Inputs received successfully!")

    st.write("Name:", name)
    st.write("Role:", role)
    st.write("Skills:", skills)
    st.write("Experience:", experience)
