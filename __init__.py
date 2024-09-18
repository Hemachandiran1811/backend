import azure.functions as func
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPI running in Azure Functions!"}

async def main(req: func.HttpRequest, context: func.Context):
    return await func.AsgiMiddleware(app).handle(req, context)
