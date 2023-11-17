from pydantic import BaseModel
from datetime import datetime

class MoistureData(BaseModel):
    device_id:str
    mc:float
    create_on: datetime 
    
