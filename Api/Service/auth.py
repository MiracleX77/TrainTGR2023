from fastapi import HTTPException
from Model.auth import RegisterData,LoginData,UserData
from Repository.user import UserRepository


class RegisterService:
    
    @staticmethod
    async def verifyData(data:RegisterData):
        user = await UserRepository.getOneByUsername(data.username)
        if user :
            raise HTTPException(status_code=400,detail="User Already")
        
        user = await UserRepository.getOneByEmail(data.email)
        if user :
            raise HTTPException(status_code=400,detail="Email Already")
        
    @staticmethod
    async def register(data:RegisterData):
        userData = UserData(firstname=data.firstname,lastname=data.lastname,username=data.username,password=data.password,email=data.email)
        user = await UserRepository.create(userData)
        if user == False:
            raise HTTPException(status_code=500,detail="ERR: Register Fail")

class LoginService:
    @staticmethod
    async def verifyData(data:LoginData):
        user = await UserRepository.getOneByUsername(data.username)
        if user == False:
            raise HTTPException(status_code=400,detail="User Not Found")
        if user["password"] != data.password:
            raise HTTPException(status_code=400,detail="Password Not Match")
        