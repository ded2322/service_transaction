from fastapi import FastAPI

from user_microservice.router import router_auth

app = FastAPI(title="Auth service", version="1")

app.include_router(router_auth)
