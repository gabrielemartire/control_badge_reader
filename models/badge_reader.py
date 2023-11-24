from models.base import Base, badge_readers_roles, badge_readers_warnings
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timedelta

class BadgeReader(Base):
    __tablename__ = "badge_readers"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    label: Mapped[str] = mapped_column(String(30), nullable=False)
    maintenance_at: Mapped[str] = mapped_column(String(30), nullable=False, default=(datetime.now() + timedelta(days=365 * 2)))
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(String(30), nullable=True)
    sector_id: Mapped[int] = mapped_column(ForeignKey("sectors.id"))
    access = relationship("Access", back_populates="badge_reader") # badge reader 1-n access
    sector = relationship("Sector", back_populates="badge_reader") # badge reader n-1 sector
    roles = relationship('Role', secondary=badge_readers_roles, back_populates='badge_readers') # badge reader n-n roles
    warning = relationship('Warning', secondary=badge_readers_warnings, back_populates='badge_readers') # badge reader n-n warnings
