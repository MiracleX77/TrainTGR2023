from Config.Connection import mongo_connected
from bson.objectid import ObjectId
from Model.auth import RegisterData, UserData
class UserRepository:
    @staticmethod
    async def getOneById(id:str):
        user = mongo_connected.collection("User").find_one({"_id": ObjectId(id)})
        if user:
            return user
        else:
            return False
    
    @staticmethod
    async def getOneByUsername(username:str):
        user = mongo_connected.collection("User").find_one({"username": username})
        if user:
            return user
        else:
            return False
        
    @staticmethod
    async def getOneByEmail(email:str):
        user = mongo_connected.collection("User").find_one({"email": email})
        if user:
            return user
        else:
            return False
        
    @staticmethod    
    async def create(data:UserData):
        user = mongo_connected.collection("User").insert_one(data.model_dump())
        if user:
            return user
        else:
            return False