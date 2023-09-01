import streamlit as st
from gtts import gTTS
def text_to_speech(text, language='zh-cn'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")

# tampilan ui    
st.title("gTTS by Marvel")
text = st.text_input("put your text/question here")
language = st.selectbox("Pls select your language", ("zh-CN", "id", "pt", "fr") )
if st.button("play"):
    text_to_speech(text, language)                   

            