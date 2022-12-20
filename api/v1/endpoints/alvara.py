from typing import Optional
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from fastapi import Response
from fastapi import Request
from fastapi.responses import JSONResponse

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from models.usuario_model import UsuarioModel
from schemas.usuario_schema import *
from core.deps import get_current_user



router = APIRouter()


@router.get('/webhook', status_code=status.HTTP_202_ACCEPTED)
async def webhook(request: Request, x_user_jwt: str = Depends(get_current_user)):
    payload = await request.json()

    return payload
    return Response(status_code=status.HTTP_202_ACCEPTED)