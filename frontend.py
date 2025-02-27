import streamlit as st


st.markdown(
    """
    <style>

    body {

    background-color:rgb(0, 0, 0);
    
    }

    h1.heading1 {

        color: rgba(223, 7, 7, 0.68);
        text-align: center;
        font-size: 100px;  /* Corrected 'fontsize' to 'font-size' */
        font-family: 'Varela Round', Rubik, Quicksand, sans-serif;
        text-shadow: 6px 6px 10px rgba(108, 24, 1, 0.77);

        position: fixed;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        padding: 20px;
        z-index: 10;

    }


    t.bodytext {

    color: rgb(38, 2, 79);
    text-align: left;
    font-family:'Varela Round', Rubik, Quicksand, sans-serif
    
    }
    </style>
    """, unsafe_allow_html=True)




def homepage():
    st.markdown('<h1 class="heading1">StemFlow</h1>', unsafe_allow_html=True)
    st.markdown('<t class="bodytext">StemFlow is a high-level machine learning, source separation based model that uses deep neural networks to split musical compositions into individual track stems. Go to "about StemFlow" for more information. </t>', unsafe_allow_html=True)
def about_stemflow():
     st.markdown('<h1 class="heading1">About StemFlow</h1>', unsafe_allow_html=True)
     st.markdown('<t class="bodytext">StemFlow operates using the demucs model(created by Meta) the repository of which can be found below;</t>')
     st.markdown("[Demucs Repository](https://github.com/facebookresearch/demucs)")
     st.markdown('<t class="bodytext">The demucs stem splitter uses a U-Net architecture to make it extremely effective. U-Net architecture uses an encoder-decoder system. The encoder extracts features from the input (the mixed audio) and reduces its dimensionality. The decoder then reconstructs the individual sources from these features. The key innovation about the U-Net is the skip connections, which can allow fine details to be preserved.</t>')
     st.markdown('<t class="bodytext">Another feature that Demucs employs is Recurrent Neural Networks. This is especially useful for stem splitting as they can access past data and use it to make predictions for what is going to happen next. This makes it extremely efficient at splitting tracks, as it can recognise and predict what sounds each instrument in the song is going to make next. </t>')
     st.image(rnn.png)
