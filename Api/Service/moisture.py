import json
from typing import List
from fastapi import HTTPException
from Repository.moisture import MoistureRepository
from Repository.device import DeviceRepository

class MoistureService:
    @staticmethod
    async def getLastMoistureByDeviceId(deviceId:str):
        moisture = await MoistureRepository.getOneByDeviceId(deviceId=deviceId)
        if moisture:
            moisture= json.loads(json.dumps(moisture,default=str))
            return moisture
        else:
            raise HTTPException(status_code=400,detail="Moisture Not Found")
    
    @staticmethod
    async def getAllLastMoistureListDeviceId(list_device_id:List[str]):
        list_moisture = []
        for device_id in list_device_id:
            
            moisture = await MoistureRepository.getOneByDeviceId(deviceId=device_id)
            if moisture == False:
                raise HTTPException(status_code=400,detail="Device Not Found")
            list_moisture.append({"device_id":device_id,"moisture":moisture["mc"],"timestamp":moisture["timestamp"]})
        
        if list_moisture:
            return list_moisture
        else:
            raise HTTPException(status_code=400,detail="Moisture Not Found")