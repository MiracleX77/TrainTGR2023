from fastapi import APIRouter,HTTPException

from Model.response import ResponseData
from Service.device import DeviceService
from Model.device import DeviceData

router = APIRouter(
    prefix="/api/device",
    tags =["device"],
    responses={404:{"description":"Not found"}},
)

@router.post("/createDevice",response_model=ResponseData,response_model_exclude_none=True)
async def createDevice(data:DeviceData):
    await DeviceService.verifyData(data=data)
    await DeviceService.createDevice(data=data)
    return ResponseData(detail="Create Device Success")

@router.get("/getDevicesByUserId/{userId}",response_model=ResponseData,response_model_exclude_none=True)
async def getDevicesByUserId(userId:str):
    device = await DeviceService.getDevicesByUserId(userId=userId)
    return ResponseData(detail="Get Device Success",result=device)

