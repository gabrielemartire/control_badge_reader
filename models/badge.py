from models.base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from datetime import datetime

class Badge(Base):
    __tablename__ = "badges"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), unique=True, nullable=True)
    created_at: Mapped[str] = mapped_column(String(100), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(100), nullable=True)
    user = relationship('User', back_populates='badge')
    access = relationship('Access', back_populates='badge')
