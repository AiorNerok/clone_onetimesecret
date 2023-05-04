from pydantic import BaseModel


__all__ = ["PongSchemas"]


class PongSchemas(BaseModel):
    message: str
