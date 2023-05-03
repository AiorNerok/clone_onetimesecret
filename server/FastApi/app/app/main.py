"""Main File"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/ping')
async def ping():
    """Test Connect

    Returns:
        "message": "pong"
    """
    return {
        'message': 'pong'
    }
