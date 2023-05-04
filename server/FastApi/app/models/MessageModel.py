from sqlmodel import SQLModel, Field


class MessageModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    message: str = Field(nullable=False)
    key: str = Field(nullable=False)
