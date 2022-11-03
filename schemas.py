from pydantic import BaseModel
from enum import Enum

class Input(BaseModel):
    operation_type: str
    x: int
    y: int 

    class Config:
        extra = "forbid" # I don't want my endpoint accepting surplus values.
