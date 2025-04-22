import streamlit as st
import langchain_helper

st.title("Restraunt Name generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "American", "Mexican", "Spinach", "Pakistani", "Bangladeshi"))

if (cuisine):
    loading_placeholder = st.empty()
    loading_placeholder.header("Loading. . . ")
    response = langchain_helper.generate_res(cuisine)
    print(response)
    loading_placeholder.empty()
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')

    for i in menu_items: 
        st.write("-", i)