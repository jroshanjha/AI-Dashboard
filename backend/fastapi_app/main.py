from fastapi import FastAPI, UploadFile, File
from nlp import process_text
from image import analyze_image
from pdf import analyze_pdf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Engine Running"}

@app.post("/nlp")
async def nlp_task(text: str):
    return process_text(text)

@app.post("/image")
async def image_task(file: UploadFile = File(...)):
    return await analyze_image(file)

@app.post("/pdf")
async def pdf_task(file: UploadFile = File(...)):
    return await analyze_pdf(file)