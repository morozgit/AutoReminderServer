from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class PartsModels(Base):
    __tablename__ = "parts"

    part_id: Mapped[int] = mapped_column(primary_key=True)
    part_name: Mapped[str] = mapped_column(String(255), nullable=False)
    mileage: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<PartsModels(id={self.part_id}, name={self.part_name})>"