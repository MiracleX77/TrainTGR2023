import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient
import os
from datetime import datetime


username = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
mongoClient  = MongoClient(f"mongodb://{username}:{password}@TGR-mongo-1:27017/")

db = mongoClient['TGR']
sensorCollection = db['Moisture']
summeryCollection = db['MoistureSummery']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("tgr_sensor/#")
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)
    topic = msg.topic.split("/")[-1]
    list_sensor = ['655631c654cc6ac08fa21fab', '655632a79a0c48b0dfe9b982']
    if (topic in list_sensor):
        record = {
            "device_id": topic,
            "mc": data['mc'],
            "timestamp": datetime.now(),
        }
        sensorCollection.insert_one(record)
        
        existing_data = summeryCollection.find_one({"device_id": topic})
        
        if existing_data:
            summeryCollection.update_one(
                {"device_id": topic},
                {
                    "$set": {
                        "mc": data['mc'],
                        "timestamp": datetime.now()
                    }
                }
            )
        else:
            record = {
                "device_id": topic,
                "mc": data['mc'],
                "timestamp": datetime.now(),
            }
            summeryCollection.insert_one(record)
    
if __name__ == '__main__':
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883,60)
    
    client.loop_forever()