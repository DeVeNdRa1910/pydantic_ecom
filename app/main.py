from fastapi import FastAPI, Request
from app.api.v1 import products
from dotenv import load_dotenv
import os 

load_dotenv()
app = FastAPI()

@app.middleware("http")
async def lifecycle(request: Request, call_next):
    print("Before")
    reseponse = await call_next(request)
    print("After")
    return reseponse

app.include_router(products.router, prefix="/products", tags=["product"])