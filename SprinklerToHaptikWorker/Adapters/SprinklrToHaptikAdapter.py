from ..Models.HaptikUserCreateModel import HaptikUserCreateModel
from ..Models.HaptikMessageModel import HaptikPayloadModel
import logging


class Adapter:

    def __init__(self, payloadJson):
        self.payload = payloadJson

    def toHaptikPayloadModel(self):
        payLoadModel = HaptikPayloadModel(self.payload)
        logging.info("Converted to HaptikPayLoadModel")
        return payLoadModel

    def toHaptikCreateUserModel(self):
        createUserModel = HaptikUserCreateModel(self.payload)
        logging.info("Converted to HaptikUserCreateModel")
        return createUserModel
