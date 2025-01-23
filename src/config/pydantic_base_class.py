from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field


class MultiQuerySchema(BaseModel):
    Questions: List[str] = Field(description="List of questions")
