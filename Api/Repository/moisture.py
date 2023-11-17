from Config.Connection import mongo_connected

class MoistureRepository :
    @staticmethod
    async def getOneByDeviceId(deviceId:str):
        moisture = mongo_connected.collection("MoistureSummery").find_one({"device_id": deviceId})

        return moisture
