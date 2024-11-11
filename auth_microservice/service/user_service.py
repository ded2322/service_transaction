from auth_microservice.utils.auth import DecodeJWT,get_password_hash
from auth_microservice.schemas.users_schemas import JWTTokenSchema, UserUpdateDataSchema
from auth_microservice.validator.user_validator import UserValidator, AuthCheck
from auth_microservice.orm.user_orm import UserOrm

class UserService:
    @classmethod
    async def show_all_users(cls):
        """Возвращает всех пользователей из базы данных"""
        return await UserOrm.all_users()

    @classmethod
    async def update_data_user(cls, data_update: UserUpdateDataSchema, jwt_token: JWTTokenSchema):
        """Обновляет данные пользователя на основе предоставленной информации."""

        user_data = await AuthCheck.get_user_info(id=DecodeJWT.decode_jwt(jwt_token.token))


        UserValidator.check_availability_user(user_data)

        # Собираем поля для обновления
        update_fields = {}

        if data_update.password:
            update_fields["password"] = get_password_hash(data_update.password)

        if update_fields:
            await UserOrm.update_data(id=user_data["id"], **update_fields)

        return {"message": "Data updated successfully"}
