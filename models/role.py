from models.base import Base, badge_readers_roles
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    label: Mapped[str] = mapped_column(String(30), nullable=False)
    night_availability: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(30), nullable=True)
    user = relationship("User", back_populates="role")
    sector = relationship("Sector", back_populates="role")
    badge_readers = relationship('BadgeReader', secondary=badge_readers_roles, back_populates='roles' )