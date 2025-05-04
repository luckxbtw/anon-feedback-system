from sqlalchemy import Column, Integer, String, DateTime, Enum, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class FeedbackType(enum.Enum):
    idea = "idea"
    complaint = "complaint"
    thanks = "thanks"
    other = "other"

class FeedbackStatus(enum.Enum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(2000), nullable=False)
    type = Column(Enum(FeedbackType), nullable=False)
    tags = Column(ARRAY(String), default=[])
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(FeedbackStatus), default=FeedbackStatus.new)


class UserRole(enum.Enum):
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.admin, nullable=False)

