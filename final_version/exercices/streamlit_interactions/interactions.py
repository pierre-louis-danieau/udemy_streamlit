import streamlit as st
import numpy as np
import pandas as pd
import datetime

def button():
    st.header("Button")
    button = st.button('click on me')
    st.write(f"Click status : {button}")

def checkbox():
    st.header("Checkbox")
    checkbox = st.checkbox('I agree')
    st.write(f"Checkbox status : {checkbox}")

def diff_button_checkox():
    st.header("Difference between button and checkbox")
    st.write(" The value of a button is re-initialized at each new run of the application. And as by default a streamlit application is restarted after each interaction with the user, this will force the value of a button to return to its default value (False). While for a checkbox, the value is kept between 2 successive runs of the application. The use of a checkbox or a button depends on the use you want to make. ")

def radio_button():
    st.header("Radio Buton")
    color = st.radio(
    "What's your favorite color",
    ('Green', 'Red', 'Blue'),
    index = 1)
    st.write(f"Your favorite color is : {color}")

def select_box():
    st.header("Select box")
    color = st.selectbox(
    "What's your favorite color",
    ('Green', 'Red', 'Blue'),
    index = 1)
    st.write(f"Your favorite color is : {color}")

def multi_select():
    st.header("Multi Select")
    color = st.multiselect(
    "What's your favorite color",
    ('Green', 'Red', 'Blue'))
    st.write(f"Your favorite colors are : {color}")

def slider():
    st.header("Slider")
    age = st.slider('What is your decade?', 0, 101, value = 0, step = 10)
    st.write(f"I am in my {age}'s")

def number_input():
    st.header("Number input")
    number = st.number_input('Insert a number', min_value = 5, max_value = 15, step = 2)
    st.write(f'The current number is {number} ')


def date_input():
    st.header("Date input")
    date = st.date_input(
     "When's your birthday",
     datetime.date(2016, 5, 23))
    st.write(f'Your birthday is: {date}')

def camera():
    st.header("Camera input")
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture)




if __name__ == "__main__":

    st.set_page_config(
        page_title="streamlit interaction app",
        layout="centered"
    )

    st.title("Widget tutorial for streamlit")

    button()

    checkbox()

    diff_button_checkox()

    radio_button()

    select_box()

    multi_select()

    slider()

    number_input()

    date_input()

    camera()