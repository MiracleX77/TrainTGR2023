from typing import List
from pydantic import BaseModel
from datetime import datetime

class DeviceData(BaseModel):
    name:str
    type:str = None
    wifi:str = None
    area_lat:str
    area_long:str
    user_id:str
    status:str = "Active"
    time_watered:datetime = None
    create_on: datetime = datetime.now()
    update_on: datetime = datetime.now()
    
class DeviceRequest(BaseModel):
    name:str
    area_lat:str
    area_long:str
    user_id:str
    
class DeviceList(BaseModel):
    list_device_id:List[str]