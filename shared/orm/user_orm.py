from shared.orm.base_orm import BaseOrm
from shared.models.user_models import Users

class UserOrm(BaseOrm):
    model = Users