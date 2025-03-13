import streamlit as st
import os
import torch
import torchaudio
from pydub import AudioSegment
from demucs.pretrained import get_model
from demucs.apply import apply_model
from io import BytesIO
import tempfile
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
    col1,col2=st.column([0.9, 0.1])
    with col2:
        st.image("logo.png")
        st.markdown('<h1 class="heading1">StemFlow</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="heading1">StemFlow</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="bodytext">StemFlow is a high-level machine learning, source separation based model that uses deep neural networks to split musical compositions into individual track stems. Go to "about StemFlow" for more information. </t>', unsafe_allow_html=True)
def about_stemflow():
     st.markdown('<h1 class="heading1">About StemFlow</h1>', unsafe_allow_html=True)
     st.markdown('<h2 class="bodytext">StemFlow operates using the demucs model(created by Meta) the repository of which can be found below. </t>', unsafe_allow_html=True)
     st.markdown("[Demucs Repository](https://github.com/facebookresearch/demucs)")
     st.markdown('<h2 class="bodytext">The demucs stem splitter uses a U-Net architecture to make it extremely effective. U-Net architecture uses an encoder-decoder system. The encoder extracts features from the input (the mixed audio) and reduces its dimensionality. The decoder then reconstructs the individual sources from these features. The key innovation about the U-Net is the skip connections, which can allow fine details to be preserved.</t>',unsafe_allow_html=True)
     st.markdown('<h2 class="bodytext">Another feature that Demucs employs is Recurrent Neural Networks. This is especially useful for stem splitting as they can access past data and use it to make predictions for what is going to happen next. This makes it extremely efficient at splitting tracks, as it can recognise and predict what sounds each instrument in the song is going to make next.</t>',unsafe_allow_html=True)

# Model Processing
def model():
    # Load the Demucs Model
    def load_demucs_model():
        try:
            model_name = 'htdemucs'  
            model = get_model(model_name)
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            model.to(device)
            return model, device
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None, None

    # Convert Audio to WAV if Necessary
    def convert_to_wav(input_path):
        try:
            wav, sr = torchaudio.load(input_path)
            temp_wav_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
            torchaudio.save(temp_wav_path, wav, sr)
            return temp_wav_path
        except:
            try:
                audio = AudioSegment.from_file(input_path)
                temp_wav_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
                audio.export(temp_wav_path, format="wav")
                return temp_wav_path
            except Exception as e:
                st.error(f"Conversion failed: {e}")
                return None

    # Load Audio File
    def load_audio(file_path, sample_rate=44100):
        try:
            wav, sr = torchaudio.load(file_path)
            if sr != sample_rate:
                wav = torchaudio.transforms.Resample(orig_freq=sr, new_freq=sample_rate)(wav)
            return wav, sample_rate
        except Exception as e:
            st.error(f"Error loading audio: {e}")
            return None, None

    # Perform Stem Separation
    def separate_stems(model, wav, device):
        try:
            wav = wav.unsqueeze(0).to(device)  
            model.eval()
            with torch.no_grad():
                stems = apply_model(model, wav)  
            return stems
        except Exception as e:
            st.error(f"Error during separation: {e}")
            return None

    # Save Stems
    def save_stems_as_bytes(stems, sample_rate, stem_names):
        stem_files = {}
        for idx, stem in enumerate(stems):
            try:
                buffer = BytesIO()
                torchaudio.save(buffer, stem.cpu(), sample_rate, format="wav")
                buffer.seek(0)
                stem_files[stem_names[idx]] = buffer
            except Exception as e:
                st.error(f"Error saving {stem_names[idx]}: {e}")
        return stem_files

    # Streamlit UI Setup
    def main():
        st.title("Effortless Music Demixing Tool")

        uploaded_files = st.file_uploader("Upload audio files", type=["mp3", "wav", "flac"], accept_multiple_files=True)

        if uploaded_files:
            model, device = load_demucs_model()
            if model is None:
                return

            for uploaded_file in uploaded_files:
                st.subheader(f"Processing: {uploaded_file.name}")

                temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}").name
                with open(temp_file_path, "wb") as temp_file:
                    temp_file.write(uploaded_file.read())

                wav_file_path = convert_to_wav(temp_file_path)
                if not wav_file_path:
                    continue

                wav, sample_rate = load_audio(wav_file_path)
                if wav is None:
                    continue

                with st.spinner("AI is processing your file..."):
                    stems = separate_stems(model, wav, device)
                    if stems is None:
                        continue

                stem_names = ["drums", "bass", "other", "vocals"]
                stem_files = save_stems_as_bytes(stems, sample_rate, stem_names)

                st.success(f"Stem separation complete for {uploaded_file.name}!")
                for name, buffer in stem_files.items():
                    st.audio(buffer, format="audio/wav")
                    st.download_button(f"Download {name}", buffer, file_name=f"{uploaded_file.name}_{name}.wav")

                os.unlink(temp_file_path)
                os.unlink(wav_file_path)

    main()

# Sidebar Navigation
page = st.sidebar.radio("Navigate:", ("Home", "About StemFlow", "StemFlow Model"))
st.sidebar.markdown("---")

if page == "Home":
    homepage()
elif page == "About StemFlow":
    about_stemflow()
elif page == "StemFlow Model":
    model()
