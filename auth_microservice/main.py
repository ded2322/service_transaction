from fastapi import FastAPI

from auth_microservice.api.router import router_auth, router_user

app = FastAPI(title="Auth service", version="1")

app.include_router(router_auth)
app.include_router(router_user)