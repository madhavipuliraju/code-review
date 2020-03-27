import os
import redis
# from dotenv import load_dotenv


class CacheOperations:
    def __init__(self, payloadJson):
        HOST_NAME = os.environ["host_name"]
        ACCESS_KEY = os.environ["access_key"]
        self.redisConn = redis.StrictRedis(
            host=HOST_NAME, port=6380, password=ACCESS_KEY,
            ssl=True)
        user = payloadJson.get("user")
        self.key = user["auth_id"]

    def get(self):
        value = self.redisConn.get(self.key)
        return value

    def flushCacheByKey(self):
        status = self.redisConn.__delitem__(self.key)
        return status

    def checkIfExists(self):
        result = True if self.redisConn.exists(self.key) else False
        return result

    def getThreadControl(self):
        control = self.redisConn.get(self.key+"control")
        return control

    def setThreadControl(self):
        status = self.redisConn.set(self.key+"control", "haptik")
        return status
