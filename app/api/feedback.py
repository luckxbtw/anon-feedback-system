from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.feedback import FeedbackCreate, FeedbackOut, FeedbackStatusUpdate
from app.crud import feedback as crud_feedback

router = APIRouter(prefix="/api/feedback", tags=["Feedback"])


@router.post("/", response_model=FeedbackOut, status_code=status.HTTP_201_CREATED)
async def create_feedback(data: FeedbackCreate, db: AsyncSession = Depends(get_db)):
    return await crud_feedback.create_feedback(db, data)


@router.get("/", response_model=List[FeedbackOut])
async def list_feedback(db: AsyncSession = Depends(get_db)):
    return await crud_feedback.get_all_feedback(db)


@router.get("/{feedback_id}", response_model=FeedbackOut)
async def get_feedback(feedback_id: int, db: AsyncSession = Depends(get_db)):
    feedback = await crud_feedback.get_feedback_by_id(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback


@router.patch("/{feedback_id}", response_model=FeedbackOut)
async def update_status(feedback_id: int, update_data: FeedbackStatusUpdate, db: AsyncSession = Depends(get_db)):
    feedback = await crud_feedback.update_feedback_status(db, feedback_id, update_data.status)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback