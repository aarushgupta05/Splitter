import streamlit as st
import time

import streamlit as st


st.markdown(
    """
    <style>

    
    h1.heading1 {

    color: rgba(187, 47, 133, 1);

    text-align: center;

    font-size: 100px;  /* Reduce font size */

    font-family: 'Varela Round', Rubik, Quicksand, sans-serif;

    text-shadow: 6px 6px 10px rgba(37, 0, 100, 0.8);

    margin-top: 20px; 

    padding: 10px;

    width: 100%;

    }
    </style>
    """, unsafe_allow_html=True)



def homepage():
    st.markdown('<h1 class="heading1">StemFlow</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="bodytext">StemFlow is a high-level machine learning, source separation based model that uses deep neural networks to split musical compositions into individual track stems. Go to "about StemFlow" for more information. </t>', unsafe_allow_html=True)
    st.image("logo.png")
def about_stemflow():
     st.markdown('<h1 class="heading1">About StemFlow</h1>', unsafe_allow_html=True)
     st.markdown('<h2 class="bodytext">StemFlow operates using the demucs model(created by Meta) the repository of which can be found below. </t>', unsafe_allow_html=True)
     st.markdown("[Demucs Repository](https://github.com/facebookresearch/demucs)")
     st.markdown('<h2 class="bodytext">The demucs stem splitter uses a U-Net architecture to make it extremely effective. U-Net architecture uses an encoder-decoder system. The encoder extracts features from the input (the mixed audio) and reduces its dimensionality. The decoder then reconstructs the individual sources from these features. The key innovation about the U-Net is the skip connections, which can allow fine details to be preserved.</t>',unsafe_allow_html=True)
     st.markdown('<h2 class="bodytext">Another feature that Demucs employs is Recurrent Neural Networks. This is especially useful for stem splitting as they can access past data and use it to make predictions for what is going to happen next. This makes it extremely efficient at splitting tracks, as it can recognise and predict what sounds each instrument in the song is going to make next.</t>',unsafe_allow_html=True)

page = st.sidebar.radio("Navigate:", ("Home", "About StemFlow"))
st.sidebar.markdown("---")

if page=="Home":
     homepage()

if page=="About StemFlow":
     about_stemflow()
