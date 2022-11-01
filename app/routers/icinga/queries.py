from fastapi import APIRouter, File, HTTPException, Query, UploadFile, status

router = APIRouter()

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def get_images_by_id() -> dict:
    return {f" Hello world"}

