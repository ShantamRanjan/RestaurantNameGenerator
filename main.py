import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Select a cuisine type", ["Italian", "Chinese", "Mexican", "Indian", "American"])
def generate_restaurant_name_and_item(cuisine):
    return {
        'Restaurant_name': 'Curry Delight',
        'menu_item': 'Butter Chicken',
    }
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_item(cuisine)
    st.header(response['Restaurant name'].strip())
    menu_item = response['Menu items'].strip().split(",")
    st.write("**Menu Items**")
for item in menu_item:
    st.write("-", item)
