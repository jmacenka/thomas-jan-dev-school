# Message class
# Created by Jan Macenka @ 24 Apr 2023
from pydantic import BaseModel


class Message(BaseModel):
    to_number: str
    message: str
