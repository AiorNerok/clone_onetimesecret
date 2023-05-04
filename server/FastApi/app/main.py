"""Main File"""
from fastapi import FastAPI

from api.message.router import router

from schemas import PongSchemas


server = FastAPI()

server.include_router(router=router)


@server.get("/ping", response_model=PongSchemas)
async def ping():
    """Test Connect

    Returns:
        "message": "pong"
    """
    return {"message": "pong"}
