from fastapi import FastAPI

from src import server

app = FastAPI()
app.include_router(server.router)