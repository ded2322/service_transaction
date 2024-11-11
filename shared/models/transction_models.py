from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from shared.database import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(length=10), nullable=True)