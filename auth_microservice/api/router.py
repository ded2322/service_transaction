from fastapi import APIRouter, Response


from auth_microservice.service.auth_service import AuthService
from auth_microservice.service.user_service import UserService
from auth_microservice.schemas.users_schemas import (JWTTokenSchema, UserDataLoginSchema,
                                        UserDataRegisterSchema,
                                        UserUpdateDataSchema)


#from core.logs.logs import logger_response


router_auth = APIRouter(prefix="/auth", tags=["Reg/Auth"])

router_user = APIRouter(prefix="/user", tags=["User account"])


@router_auth.post("/register", status_code=201, summary="Register user")
async def register_user(data_user: UserDataRegisterSchema):
    """Регистрация пользователя"""
    #todo verifivation email (?)
    #logger_response.info("User registered")
    return await AuthService.register_user(data_user)


@router_auth.post("/login", status_code=200, summary="Login user")
async def login_user(response: Response, data_user: UserDataLoginSchema):
    """Аутентификация пользователя"""
    # logger_response.info("User is login")
    return await AuthService.login_user(response,data_user)



@router_user.patch("/update", status_code=201, summary="Update data user")
async def update_data_user(
    jwt_token: JWTTokenSchema, data_update: UserUpdateDataSchema
):
    """Обновляет данные пользователя"""
    # logger_response.info("User update data")
    return await UserService.update_data_user(data_update, jwt_token)
