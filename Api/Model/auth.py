from pydantic import BaseModel
from datetime import datetime


class UserData(BaseModel):
    firstname:str 
    lastname:str 
    phone:str = None
    username:str  
    password:str
    email:str 
    create_on: datetime = datetime.now()
    update_on: datetime = datetime.now()
    status :str = "Active"
    
class RegisterData(BaseModel):
    username:str  
    password:str
    email:str 
    firstname:str 
    lastname:str
    
class LoginData(BaseModel):
    username:str
    password:str