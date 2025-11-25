
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import whisper
import os
import random
from ai_module import AdaptiveAI

app = FastAPI()

# Load Whisper model (base)
model = whisper.load_model("base")

# Simulated devices
devices = [{"name": "Lamp Bedroom", "type": "lamp", "state": "off"},
           {"name": "Speaker Bedroom", "type": "speaker", "state": "off"}]

ai = AdaptiveAI()

class Command(BaseModel):
    text: str

@app.get("/devices")
async def get_devices():
    return JSONResponse(content=devices)

@app.get("/scenarios")
async def get_scenarios():
    return JSONResponse(content=ai.scenarios)

@app.post("/voice")
async def voice_command(cmd: Command):
    response = ai.process_command(cmd.text)
    return {"response": response}

@app.post("/voice-audio")
async def voice_audio(file: UploadFile = File(...)):
    audio_path = f"temp_{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())
    result = model.transcribe(audio_path)
    os.remove(audio_path)
    return {"transcription": result['text']}

@app.get("/simulate")
async def simulate():
    scenario = ai.get_next_scenario()
    return {"scenario": scenario}
