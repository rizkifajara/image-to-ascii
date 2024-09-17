import re
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
from PIL import Image
import io
import ascii_magic

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def remove_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def image_to_ascii(image):
    output = ascii_magic.from_pillow_image(image)
    ascii_art = output.to_ascii()
    return remove_ansi_codes(ascii_art)

@app.post("/convert")
async def convert_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    ascii_art = image_to_ascii(image)
    return PlainTextResponse(content=ascii_art)

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})