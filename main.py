import imp
from fastapi import FastAPI

app = FastAPI() 

from product_recommendations import *


@app.get("/") 
async def root():
    a = 3
    b = 4 
    return {"message": test()}


def add(a,b):
    return a+b
