from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from shared.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(length=200), nullable=False)
    #email:Mapped[str] = mapped_column(String(length=200), nullable=False)
    #verifivation: Mapped[Boolean] = mapped_column(Boolean,default=True)
    def __str__(self):
        return f"Name: {self.name}"
