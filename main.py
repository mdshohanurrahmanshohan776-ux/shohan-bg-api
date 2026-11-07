from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import new_session, remove
import io

app = FastAPI()

# 🎯 ৫১২MB মেমোরির জন্য অপটিমাইজড মডেল (যা কখনো ক্র্যাশ করবে না)
session = new_session("u2netp")

@app.get("/")
def home():
    return {"status": "Shohan BG API on Render is Live! 🚀"}

@app.post("/remove")
async def remove_bg(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes, session=session)
    return Response(content=output_bytes, media_type="image/png")
