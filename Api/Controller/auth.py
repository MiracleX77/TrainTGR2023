

from fastapi import APIRouter,HTTPException
from Model.response import ResponseData
from Model.auth import RegisterData,LoginData
from Service.auth import RegisterService,LoginService

router = APIRouter(
    prefix="/api/auth",
    tags =["auth"],
    responses={404:{"description":"Not found"}},
)

@router.post("/register",response_model=ResponseData,response_model_exclude_none=True)
async def register(data : RegisterData):
    await RegisterService.verifyData(data=data)
    await RegisterService.register(data=data)
    return ResponseData(detail="Register Success")

@router.post("/login",response_model=ResponseData,response_model_exclude_none=True)
async def login(data:LoginData):
    await LoginService.verifyData(data=data)
    return ResponseData(detail="Login Success")