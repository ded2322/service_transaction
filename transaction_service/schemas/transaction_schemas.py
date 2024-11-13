from pydantic import BaseModel

class TransactionCreate(BaseModel):
    jwt_token: str
    id_catcher: int
    amount: float
