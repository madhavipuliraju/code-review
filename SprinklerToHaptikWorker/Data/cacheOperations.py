import redis
import os
import logging


class CacheOperations:
    def __init__(self, payloadJson):
        self.redisConn = redis.StrictRedis(
            host=os.environ["host_name"],
            port=6380, password=os.environ["access_key"],
            ssl=True)
        logging.info("Redis Connection:" + str(self.redisConn.ping()))
        receiverProfile = payloadJson.get("receiverProfile")
        self.key = receiverProfile["channelId"]
        self.value = payloadJson.get("messageId")

    def insert(self):
        status = self.redisConn.set(self.key, self.value, ex=480)
        logging.info(
            "Inserted" + self.key + ", " + self.value +
            "into redis cache:" + str(status))
        return status

    def updateValidityByMins(self, mins):
        status = self.redisConn.expire(self.key, 60*mins)
        logging.info(
            "Refreshed validity for entry " + self.key + ": " + str(status))
        return status

    def updateValidityByDays(self, days):
        status = self.redisConn.expire(self.key, 86400*days)
        logging.info(
            "Refreshed validity for entry " + self.key + ": " + str(status))
        return status

    def updateValue(self):
        status = self.redisConn.set(self.key, self.value, ex=480, xx=True)
        logging.info("Updated value with key" + self.key + ": " + str(status))
        return status

    def flushCacheByKey(self):
        status = self.redisConn.__delitem__(self.key)
        logging.info(
            "Successfully deleted entry from redis cache:" + str(status))
        return status

    def checkIfExists(self):
        result = True if self.redisConn.exists(self.key) else False
        logging.info("entry exists in cache:" + str(result))
        return result

    def getThreadControl(self):
        control = self.redisConn.get(self.key+"control")
        logging.info("Thread control with " + str(control))
        return control.decode("utf-8")

    def setThreadControl(self):
        status = self.redisConn.set(self.key+"control", "haptik")
        logging.info("Inserted threadControl into redis cache:" + str(status))
        return status
