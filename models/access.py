from models.base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Access(Base):
    __tablename__ = "accesses"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    timestamp_in: Mapped[str] = mapped_column(String(100), nullable=False, default=datetime.now)
    timestamp_out: Mapped[str] = mapped_column(String(100), nullable=False)
    badge_id: Mapped[int] = mapped_column(ForeignKey("badges.id")) # badge utilizzato per lo scan
    badge_reader_id: Mapped[int] = mapped_column(ForeignKey("badge_readers.id")) # badge reader che ha effettuato lo scan
    badge = relationship("Badge", back_populates="access") # access 1-n badge
    badge_reader = relationship("Badge_Reader", back_populates="access") # access 1-n b_r
