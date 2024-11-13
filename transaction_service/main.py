from fastapi import FastAPI

from transaction_service.api.router import router

app = FastAPI(title="Transaction service", version="1")
app.include_router(router)

