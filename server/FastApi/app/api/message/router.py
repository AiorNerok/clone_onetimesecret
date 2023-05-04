from fastapi import APIRouter,Depends
from sqlmodel import Session

from api.message.repo import MessageRepo
from db.postgres_tools import PostgresTool, get_session


router = APIRouter()

@router.get(path="/api/message/")
def get_message(db:Session=Depends(get_session)):
    return MessageRepo.get(db=db)
