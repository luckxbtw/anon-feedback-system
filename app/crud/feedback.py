from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from typing import Optional, List
from app.db.models import Feedback
from app.schemas.feedback import FeedbackCreate
from datetime import datetime


async def create_feedback(db: AsyncSession, data: FeedbackCreate) -> Feedback:
    new_feedback = Feedback(
        title=data.title,
        description=data.description,
        type=data.type,
        tags=data.tags or [],
        created_at=datetime.utcnow(),
        status="new"
    )
    db.add(new_feedback)
    await db.commit()
    await db.refresh(new_feedback)
    return new_feedback


async def get_all_feedback(db: AsyncSession) -> List[Feedback]:
    result = await db.execute(select(Feedback).order_by(Feedback.created_at.desc()))
    return result.scalars().all()


async def get_feedback_by_id(db: AsyncSession, feedback_id: int) -> Optional[Feedback]:
    result = await db.execute(select(Feedback).where(Feedback.id == feedback_id))
    return result.scalars().first()


async def update_feedback_status(db: AsyncSession, feedback_id: int, new_status: str) -> Optional[Feedback]:
    result = await db.execute(select(Feedback).where(Feedback.id == feedback_id))
    feedback = result.scalars().first()
    if feedback:
        feedback.status = new_status
        await db.commit()
        await db.refresh(feedback)
    return feedback
