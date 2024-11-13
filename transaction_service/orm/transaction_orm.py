from shared.base_orm import BaseOrm
from transaction_service.models.trasaction_models import Transactions

class TransactionOrm(BaseOrm):
    model = Transactions