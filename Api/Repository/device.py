from bson import ObjectId
from Model.device import DeviceData
from Config.Connection import mongo_connected


class DeviceRepository:
    @staticmethod
    async def getOneByName(deviceName:str,userId:str):
        device = mongo_connected.collection("Device").find_one({"name": deviceName,"user_id":userId,"status":"Active"})
        if device:
            return device
        else:
            return False
    
    @staticmethod
    async def getOneById(id:str):
        device = mongo_connected.collection("Device").find_one({"_id": ObjectId(id),"status":"Active"})
        if device:
            return device
        else:
            return False
    
    @staticmethod
    async def create(data:DeviceData):
        device = mongo_connected.collection("Device").insert_one(data.model_dump())
        if device:
            return device
        else:
            return False
        
    @staticmethod
    async def getAllByUserId(userId:str):
        device = mongo_connected.collection("Device").find({"user_id": userId,"status":"Active"})
        if device:
            return device
        else:
            return False