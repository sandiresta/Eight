import streamlit as st

st.set_page_config(page_title="Image Processing App", page_icon= r"https://github.com/sandiresta/Eight/blob/main/assets/logo%20pu.png")

st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate through the app.")

st.write("# Welcome to the Image Processing App")
img = Image.open("https://github.com/sandiresta/Eight/blob/main/assets/logo%20pu.png")
st.image(img, use_column_width=True, caption="Our Beloved University")
st.write("This is the main page. Use the menu on the left to explore different sections.")
