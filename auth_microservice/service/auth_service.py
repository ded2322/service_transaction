from fastapi import HTTPException

from auth_microservice.orm.user_orm import UserOrm
from auth_microservice.schemas.users_schemas import UserDataRegisterSchema, UserDataLoginSchema
from auth_microservice.validator.user_validator import UserValidator, AuthCheck
from auth_microservice.utils.auth import get_password_hash, create_access_token


class AuthService:
    @classmethod
    async def register_user(cls, data_user: UserDataRegisterSchema):
        """Регистрация. Создает запись пользователя в таблице users"""

        await UserValidator.validate_fields(data_user)
        await UserValidator.validate_name_availability(data_user.name)

        #validate email

        hash_password = get_password_hash(data_user.password)

        await UserOrm.insert_data(name=data_user.name, password=hash_password)

        return {"message": "User registered successfully"}


    @classmethod
    async def login_user(cls,response, data_user: UserDataLoginSchema):
        """Аутентификация пользователя и возврат токена."""

        user = await AuthCheck.get_user_info(name=data_user.name)

        if await UserValidator.validate_login_credentials(user, data_user):
                raise HTTPException(status_code=401, detail="Invalid credentials")

        
        return create_access_token({"sub": str(user["id"])})
        