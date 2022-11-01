from fastapi import APIRouter

from app.routers.icinga import queries

api_router = APIRouter()
api_router.include_router(queries.router, prefix="/icinga/api", tags=["icinga"])
