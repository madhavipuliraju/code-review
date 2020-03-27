from ..Models.SprinklrMessageModel import SprinklrPayloadModel


class Adapter:

    def __init__(self, payloadJson):
        self.payload = payloadJson

    def toSprinklrPayloadModel(self, messageId):
        payLoadModel = SprinklrPayloadModel(self.payload, messageId)
        return payLoadModel
