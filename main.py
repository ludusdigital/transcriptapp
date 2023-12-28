import streamlit as st
from openai import OpenAI
import os

api_key = os.environ['openai_api_key']

client = OpenAI(api_key=api_key)

st.title("Ludus AI Transkript App")

audio_file = st.file_uploader("Dodajte audio fajl do 25MB", type=["mp3", "wav", "m4a", "mp4"])

if st.button("TRANSKRIPTUJ"):
  if audio_file is not None:
    # Sačuvajte fajl lokalno
    audio_path = audio_file.name
    with open(audio_path, "wb") as f:
      f.write(audio_file.getbuffer())

    st.success("Fajl se transkriptuje")

    # Slanje audio fajla na OpenAI Whisper API
    with open(audio_path, "rb") as audio:
      response = client.audio.transcriptions.create(model="whisper-1", file=audio)

    # Prikaz rezultata transkripcije
    st.success("Transkripcija završena")
    st.markdown(response.text)

  else:
    st.warning("Molimo dodajte audio fajl")
