from fastapi import APIRouter

from api.message.repo import MessageRepo


router = APIRouter()


@router.get(path="/api/message/")
def get_message():
    r = MessageRepo.get()
    return r
