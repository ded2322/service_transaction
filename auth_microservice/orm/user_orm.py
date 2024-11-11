from shared.orm.base_orm import BaseOrm
from auth_microservice.models.user_models import Users

class UserOrm(BaseOrm):
    model = Users