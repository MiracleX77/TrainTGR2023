import json


from fastapi import HTTPException
from Model.device import DeviceData,DeviceRequest
from Repository.device import DeviceRepository
from Repository.user import UserRepository


class DeviceService:
    @staticmethod
    async def createDevice(data:DeviceRequest):
        deviceData = DeviceData(name=data.name,area_lat=data.area_lat,area_long=data.area_long,user_id=data.user_id)
        device = await DeviceRepository.create(deviceData)
        if device == False:
            raise HTTPException(status_code=500,detail="ERR: Create Device Fail")
        
    
    @staticmethod
    async def verifyData(data:DeviceRequest):
        user = await UserRepository.getOneById(data.user_id)
        if user == False:
            raise HTTPException(status_code=400,detail="User Not Found")
        device = await DeviceRepository.getOneByName(data.name,data.user_id)
        if device :
                raise HTTPException(status_code=400,detail="Device Name Already")

    @staticmethod
    async def getDevicesByUserId(userId:str):
        devices = await DeviceRepository.getAllByUserId(userId)
        if devices == False:
            raise HTTPException(status_code=400,detail="Device Not Found")
        devices_list = []
        for device in devices:
            device = json.loads(json.dumps(device,default=str))
            devices_list.append(device)
            
        return devices_list