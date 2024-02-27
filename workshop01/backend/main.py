from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from random import choice
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Serve static files (HTML, CSS, JS, Images) - assuming your frontend files are in a directory named 'frontend'
app.mount("/static", StaticFiles(directory="./workshop01/frontend"), name="static")

headers = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@app.get("/api/header")
async def get_header():
    return {"header": choice(headers)}

@app.get("/")
async def main():
    return HTMLResponse(open("./workshop01/frontend/index.html").read())
