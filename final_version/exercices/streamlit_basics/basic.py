import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def connect_data_csv():
    st.header("Streamlit connect data tutorial")

    ### PUT YOUR OWN PATH BELOW ####
    MY_PATH = '/Users/pierre-louis.danieau/Desktop/udemy_streamlit/initial_version/project/s&p500.csv'
    ################################

    data = pd.read_csv(MY_PATH)
    st.dataframe(data)

    st.dataframe(data.style.highlight_max(axis=0))

def display_write():
    st.header("Streamlit display text tutorial")
    st.title("Title of my super app")

    st.header("Header of my app")

    st.subheader("Sub header of my app")

    st.write("Any text to explain something")

    st.caption("Any information")

    code = '''def hello(): 
    print("Hello, Streamlit!")'''
    st.code(code, language='python')

    st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"HTML text green"}</h1>', unsafe_allow_html=True)


def display_media():
    st.header("Streamlit display media tutorial")

    st.header("Image")
    image = Image.open('final_version/exercices/streamlit_basics/stock.jpeg')

    st.image(image, caption='@austindistel', width = 250)

    st.header("Audio")
    audio_file = open('final_version/exercices/streamlit_basics/audio.ogg', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
    st.write("Audio credit:  Performer: Muriel Nguyen Xuan and Stéphane Magnenat / Composer: Frédéric Chopin")
    st.write("URL: https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")

    st.header("Video")
    video_file = open('final_version/exercices/streamlit_basics/video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.write("Creator: User fxxu from Pixabay.")
    st.write("URL: https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/")

def layout():
    st.header("Streamlit layout tutorial")

    # Sidebar
    st.sidebar.title("Sidebar title ")
    st.sidebar.write("You can add all components by applying the 'st' object just before it")
    st.sidebar.metric(label="Sidebar Temperature metrics", value="25 °", delta="2.1 °")

    # Columns
    col1, col2 = st.columns(2)
    with col1:
        st.header("First column")
        st.write("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col2:
        st.header("Second column")
        st.write("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    # Containers
    with st.container():
        st.header("1st container")
        st.bar_chart(np.random.randn(50, 3))

    with st.container():
        st.header("2nd container")
        st.dataframe(pd.DataFrame(np.random.randn(3, 2)))

    # Expander
    st.header('Outside of containers')
    with st.expander("This is an expander"):
     st.write("""
            Streamlit tutorial for the layout of an application
     """)



if __name__ == "__main__":

    st.set_page_config(
        page_title="streamlit basics app",
        layout="centered"
    )

    st.title("Streamlit fundamentals tutorial")

    connect_data_csv()

    display_write()

    display_media()

    layout()