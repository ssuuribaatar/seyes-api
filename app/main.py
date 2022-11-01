from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.core.event_handlers import start_app_handler, stop_app_handler
from app.routers.api import api_router

from .dependency import has_access

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def custom_openapi() -> dict:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SEYES",
        version="1.0.0",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# router
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def get_documentation(username: str = Depends(has_access)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/docs", include_in_schema=False)
async def get_documentations(username: str = Depends(has_access)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(has_access)):
    return get_openapi(title="FastAPI", version="0.1.0", routes=app.routes)


# model loader
app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))
