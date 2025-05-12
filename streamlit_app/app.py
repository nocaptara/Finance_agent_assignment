import streamlit as st
import requests
import sounddevice as sd
import wavio
import tempfile

st.title("🎙️ Morning Market Voice Assistant")

st.markdown("Press the button and ask something like: **'What’s our risk exposure in Asia tech stocks today?'**")

def record_voice(filename="input.wav", duration=5, samplerate=44100):
    st.info("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    wavio.write(filename, recording, samplerate, sampwidth=2)
    st.success("Recording complete!")

if st.button("🎤 Ask Your Question"):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        record_voice(tmp.name)
        with open(tmp.name, "rb") as f:
            files = {"file": f}
            transcript_res = requests.post("http://localhost:8005/listen", files=files)
            transcript = transcript_res.json()["transcript"]
            st.write(f"🗣️ You said: {transcript}")

            brief_res = requests.post("http://localhost:8006/morning_brief", json={"question": transcript}).json()
            st.markdown(f"**📢 System says:**\n\n> {brief_res['brief']}")
