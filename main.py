from copyreg import constructor
import imp
from fastapi import FastAPI

app = FastAPI() 

from product_recommendations import *


@app.get("/") 
async def root():
    a = 3
    b = 4 
    return {"message": test()}


@app.get("/test") 
async def root():
    print("testing")
    return {"message": "I am here"}

def add(a,b):
    return a+b
