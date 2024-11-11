from fastapi import APIRouter, Response


from user_microservice.auth_service import AuthService

from user_microservice.users_schemas import (JWTTokenSchema, UserDataLoginSchema,
                                        UserDataRegisterSchema,
                                        UserUpdateDataSchema)

#from core.services.user_service import UserService
#from core.logs.logs import logger_response


router_auth = APIRouter(prefix="/auth", tags=["Auth"])

router_user = APIRouter(prefix="/user", tags=["User"])


@router_auth.post("/register", status_code=201, summary="Register user")
async def register_user(data_user: UserDataRegisterSchema):
    """Регистрация пользователя"""
    #todo verifivation email (?)
    #logger_response.info("User registered")
    return await AuthService.register_user(data_user)


# @router_auth.post("/login", status_code=200, summary="Login user")
# async def login_user(response: Response, data_user: UserDataLoginSchema):
#     """Аутентификация пользователя"""
#     logger_response.info("User is login")
#     return await AuthService.login_user(response,data_user)



# @router_user.patch("/update", status_code=201, summary="Update data user")
# async def update_data_user(
#     jwt_token: JWTTokenSchema, data_update: UserUpdateDataSchema
# ):
#     """Обновляет данные пользователя"""
#     logger_response.info("User update data")
#     return await UserService.update_data_user(data_update, jwt_token)


# @router_user.delete("/delete", status_code=201, summary="Delete user")
# async def delete_user(jwt_token: JWTTokenSchema):
#     """Удаляет аккаунт"""
#     logger_response.info("User deleted")
#     return await UserService.delete_user(jwt_token)
