from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
from fastapi.responses import FileResponse

# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.metrics import structural_similarity as ssim

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def upload(file):
 fo = open(file, "rb")
 image=fo.read()
 fo.close()
 fo.write(image)
 fo.close()
 return (key,imageRes)

def decrypt(key,file):
 key=int(key)
 fo = open(file, "rb")
 image=fo.read()
 fo.close()
 image=bytearray(image)
 for index , value in enumerate(image):
  image[index] = value^key
 fo=open("dec.jpg","wb")
 imageRes="dec.jpg"
 fo.write(image)
 fo.close()
 return imageRes




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)): 
        with open(file.filename, "wb") as buffer:
          shutil.copyfileobj(file.file, buffer)
          path=file.filename
          %store path
          %run ./500_Testing.ipynb
          %store - r result_list
        return {'result':result_list}

@app.get("/result")
def return_file():
    return FileResponse("./enc.jpg",filename="enc.jpg")
