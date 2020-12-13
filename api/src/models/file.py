from typing import Optional

from pydantic import BaseModel


class APIFile(BaseModel):
    name: Optional[str]
    count: Optional[int]
