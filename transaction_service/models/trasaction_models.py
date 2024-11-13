import enum
from sqlalchemy import Enum, ForeignKey, Float, Date, Time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from shared.database import Base


class TransactionStatus(enum.Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    FAILED = "failed"

class Transactions(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sernder: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    catcher: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    amount: Mapped[Float] = mapped_column(Float, nullable=False)
    data_transaction: Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, index=True)
    time_transaction: Mapped[Time] = mapped_column(Time, default=func.current_time(), nullable=False, index=Time)
    status: Mapped[Enum] = mapped_column(Enum(TransactionStatus), nullable=False)