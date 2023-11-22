from models.base import Base, badge_readers_roles
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    label: Mapped[str] = mapped_column(String(100), nullable=False)
    night_availability: Mapped[bool] = mapped_column()
    created_at: Mapped[str] = mapped_column(String(100), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(100), nullable=True)
    user = relationship("User", back_populates="role") # user n-1 role
    sector = relationship("Sector", back_populates="role") # sector n-1 role
    badge_readers = relationship('BadgeReader', secondary=badge_readers_roles, back_populates='roles' ) # badge_reader n-n role