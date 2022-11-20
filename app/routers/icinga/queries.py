from fastapi import APIRouter, status
from starlette.requests import Request

router = APIRouter()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def hello_world() -> dict:
    return {f" Hello world"}


@router.get(
    "/host/summary",
    status_code=status.HTTP_200_OK,
)
async def get_host_summary(request: Request) -> dict:
    _icinga = request.app.state.icinga_instance
    _hosts = _icinga.get_host_summary()
    _summary = {
        'all': _icinga.host_count,
        'up': 6,
        'down': 1
    }
    return {
        'hosts': _hosts,
        'summary': _summary
    }

