import pyttsx3
import whisper
import tempfile
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Voice Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Allow all origins (change this for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TTS engine
tts_engine = pyttsx3.init()

# STT model (Whisper)
stt_model = whisper.load_model("base")

class VoiceRequest(BaseModel):
    text: str

@app.post("/speak")
def speak_text(request: VoiceRequest):
    tts_engine.say(request.text)
    tts_engine.runAndWait()
    return {"status": "Speaking", "text": request.text}

@app.post("/listen")
async def listen(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    result = stt_model.transcribe(tmp_path)
    return {"transcript": result["text"]}
