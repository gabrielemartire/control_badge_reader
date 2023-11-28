from models.base import Base
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(30), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(30), nullable=True)
    deleted_at: Mapped[str] = mapped_column(String(30), nullable=True)
    role = relationship("Role", back_populates="user")
    badge = relationship("Badge", back_populates="user", uselist=False, cascade="all, delete-orphan")