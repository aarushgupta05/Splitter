import streamlit as st
import time


st.markdown(
    """
    <style>
    body {
        background-color:rgba(0, 0, 0, 0);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .stButton>button {
        background-color:rgb(88, 1, 1);
        color: white;
        border-radius: 50px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color:rgb(201, 12, 138);
        box-shadow: 0 4px 8px rgba(126, 4, 122, 0.86);
    }

    .stTextInput>div>input {
        border-radius: 15px;
        padding: 10px;
        border: none;
        font-size: 14px;
    }

    .page {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        animation: fadein 1s ease-in-out;
    }

    .link {
    color: blue;
    font-size: 16px;
    
    }

    @keyframes fadein {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)


def page_one():
    st.title("Who am I?")
    st.markdown("Hello! My name is Aarush, and I am a 9th grade student at UWCSEA in Singapore. I am also an avid musician and was searching for a simple, convenvient way to separate vocals, and different instruments from my favourite songs. That's when I came across the demucs stem splitter (more on that on page2). So, I decided to make this stem splitter. One of the main things I've tried to do here is make the GUI as simple as possible-- I won't bother you with technical stuff if you don't want to be (click on page 3 if you're interested.)")
    time.sleep(1)  

def page_two():
    st.title("The Demucs Model")
    st.markdown("The Demucs Stem Splitter is a deep-learning-based model designed for music source separation, meaning it can take a mixed audio track and split it into individual stems like vocals, drums, bass, and other instruments. Developed by Meta, Demucs uses a convolutional recurrent neural network (CRNN) architecture to achieve high-quality separation, making it popular among musicians, audio engineers, and AI researchers. It significantly outperforms traditional signal-processing methods by leveraging deep learning to better preserve the natural sound of separated components.")
    st.markdown("The GitHub Repo can be found below if you would like to explore it")
    st.markdown("[Demucs GitHub Repository](https://github.com/facebookresearch/demucs)")
def page_three():
    st.title("Page 3")
    st.markdown("")
def page_four():
    st.title("Stem Splitter")

def main():
    st.sidebar.title("Navigation")
    pages = ["Page 1", "Page 2", "Page 3"]

    selection = st.sidebar.radio("Go to", pages)

    if selection == "Page 1":
        page_one()
    elif selection == "Page 2":
        page_two()
    elif selection == "Page 3":
        page_three()


if __name__ == "__main__":
    main()
