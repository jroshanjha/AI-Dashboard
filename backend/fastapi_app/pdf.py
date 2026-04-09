import fitz  # PyMuPDF

async def analyze_pdf(file):
    contents = await file.read()
    
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    doc = fitz.open("temp.pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return {"summary": text[:1000]}