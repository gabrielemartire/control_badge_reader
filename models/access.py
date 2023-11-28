from models.base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Access(Base):
    __tablename__ = "accesses"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    timestamp_in: Mapped[str] = mapped_column(String(30), nullable=True)
    timestamp_out: Mapped[str] = mapped_column(String(30), nullable=True)
    created_at: Mapped[str] = mapped_column(String(30), nullable=False, default=datetime.now)
    badge_id: Mapped[int] = mapped_column(ForeignKey("badges.id"), nullable=False)
    badge_reader_id: Mapped[int] = mapped_column(ForeignKey("badge_readers.id"), nullable=False)
    badge = relationship("Badge", back_populates="access")
    badge_reader = relationship("BadgeReader", back_populates="access")