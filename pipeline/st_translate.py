# pip install -q streamlit
import streamlit as st
from transformers import pipeline

client = pipeline("translation_en_to_hi",         
                       model="Helsinki-NLP/opus-mt-en-hi")

st.title("English to Hindi")
text  = st.text_input("Enligsh Text", "" )
if len(text) > 0:
    prompt = f"""
    Translate the following English text to simple Hindi:
    
    {text}                
    """
    hindi = client.translation(prompt)
    st.write("<h2>" + hindi.translation_text + "</h2>", unsafe_allow_html=True)



     