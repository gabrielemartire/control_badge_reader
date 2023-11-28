from models.base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Sector(Base):
    __tablename__ = "sectors"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    label: Mapped[str] = mapped_column(String(30), nullable=False)
    under_uta_control: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(30), nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    role = relationship("Role", back_populates="sector")
    badge_reader = relationship("BadgeReader", back_populates="sector")