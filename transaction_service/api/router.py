from fastapi import APIRouter, HTTPException, status

from transaction_service.schemas.transaction_schemas import TransactionCreate
from transaction_service.orm.transaction_orm import TransactionOrm
from transaction_service.models.trasaction_models import TransactionStatus

from auth_microservice.utils.auth import decode_jwt_user_id
from auth_microservice.orm.user_orm import UserOrm


router = APIRouter(prefix="/transaction", tags=["Transaction"])

@router.get("/history")
async def history_transactions():
    ...

@router.post("/create")
async def create_transaction(transaction_data: TransactionCreate):
    #decode jwt
    #found cathcer 
    #check sum sender -> if less money rejected transaction
    # create transaction
    user_id = decode_jwt_user_id(token=transaction_data.jwt_token)
    catcher_data = await UserOrm.found_one_or_none(id=transaction_data.id_catcher)
    sender_data = await UserOrm.found_one_or_none(id=user_id)

    if sender_data["amount"] < transaction_data.amount:
        await TransactionOrm.insert_data(sernder=user_id, catcher=catcher_data["id"], amount=transaction_data.amount, status=TransactionStatus.REJECTED)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ПОШЕЛ НАХУЙ ПИДОР")
    
    await UserOrm.update_data(id=user_id,amount=sender_data["amount"] - transaction_data.amount)
    await UserOrm.update_data(id=catcher_data["id"],amount=catcher_data["amount"] + transaction_data.amount)
    await TransactionOrm.insert_data(sernder=user_id, catcher=catcher_data["id"], amount=transaction_data.amount, status=TransactionStatus.ACCEPTED)

    return f"{sender_data['name']} sent {transaction_data.amount} to {catcher_data['name']}"

