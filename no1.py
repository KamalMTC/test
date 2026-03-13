import streamlit as st

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("сайт привет")
st.write("ты умрешь в муках")
st.write("на тебя наложено проклятие")
st.balloons() #
