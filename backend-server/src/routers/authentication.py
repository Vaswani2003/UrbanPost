from fastapi import APIRouter, HTTPException, status
from src.core.logging import logger
from src.viewmodels.authentication_viewmodel import (
    CreateUserRequest,
    CreateUserResponse
)
from src.services.authentication_service import handle_create_new_user


router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
    )

@router.post("/create-user",
            response_model=CreateUserResponse,
            status_code=status.HTTP_201_CREATED
            )
async def create_new_user(body: CreateUserRequest) -> CreateUserResponse:
    return await handle_create_new_user(body)
    