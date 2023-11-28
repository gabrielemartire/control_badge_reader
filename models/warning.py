from models.base import Base, badge_readers_warnings
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Warning(Base):
    __tablename__ = "warnings"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    code_name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(30), nullable=True)
    deleted_at: Mapped[str] = mapped_column(String(30), nullable=True)
    badge_readers = relationship('BadgeReader', secondary=badge_readers_warnings, back_populates='warnings' )