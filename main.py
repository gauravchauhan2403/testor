from typing import Optional
from unittest import result
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
from fastapi.responses import FileResponse
import pickle
import os

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
          file1 = open("Original.txt", "wb") 
          pickle.dump(path, file1)
          file1.close
        #   exec(open("./500_Testing.py").read()) 
          os.system('500_Testing.py')
          with open('Original1.txt', 'rb') as f:
           result_list = pickle.load(f)
        return {'result':result_list}

@app.get("/result")
def return_file():
    return FileResponse("./enc.jpg",filename="enc.jpg")
