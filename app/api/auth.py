from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserLogin, UserOut
from app.db.models import User
from app.core.security import verify_password, create_access_token
from sqlalchemy.future import select

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login", response_model=UserOut)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == credentials.email))
    user = result.scalars().first()

    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": str(user.id), "role": user.role})
    user_data = UserOut.from_orm(user)
    user_data.token = token  # Добавим вручную, если нужно
    return user_data
