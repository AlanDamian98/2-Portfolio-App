import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images\myphoto.jpg", width=300)

with col2:
    st.title("Alan Damian")
    content = """
    Solo se que nose nada..
    """
    st.info(content)


content2 = ("""
Below you can find some of the apps I have built in Python. Feel free to contact me!
""")

st.write(content2)