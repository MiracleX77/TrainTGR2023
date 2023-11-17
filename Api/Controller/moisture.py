from typing import List
from fastapi import APIRouter
from Model.response import ResponseData
from Service.moisture import MoistureService
from Model.device import DeviceList

router = APIRouter(
    prefix="/api/moisture",
    tags =["moisture"],
    responses={404:{"description":"Not found"}},
)

@router.get("/getMoistureByDeviceId/{deviceId}",response_model=ResponseData,response_model_exclude_none=True)
async def getMoistureByDeviceId(deviceId:str):
    res = await MoistureService.getLastMoistureByDeviceId(deviceId=deviceId)
    return ResponseData(detail="Get Moisture Success",result=res)

@router.post("/getAllMoistureByListDeviceId",response_model=ResponseData,response_model_exclude_none=True)
async def getAllMoistureByListDeviceId(list_device_id:DeviceList):
    res = await MoistureService.getAllLastMoistureListDeviceId(list_device_id=list_device_id.list_device_id)
    return ResponseData(detail="Get Moisture Success",result=res)