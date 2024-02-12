from fastapi import FastAPI

from coffee.router import router as router_base

app = FastAPI(
    title="Coffee shop"
)

app.include_router(router_base)


