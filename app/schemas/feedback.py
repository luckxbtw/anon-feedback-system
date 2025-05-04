from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Literal

class FeedbackBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=2000)
    type: Literal["idea", "complaint", "thanks", "other"]
    tags: Optional[list[str]] = []

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackOut(FeedbackBase):
    id: int
    created_at: datetime
    status: Literal["new", "in_progress", "resolved"] = "new"

    class Config:
        orm_mode = True

class FeedbackStatusUpdate(BaseModel):
    status: Literal["new", "in_progress", "resolved"]
