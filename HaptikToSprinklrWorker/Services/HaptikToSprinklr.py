from .SprinklrService import SprinklrService
from ..Data.cacheOperations import CacheOperations
from ..Adapters import HaptikToSprinklrAdapter


class HaptikToSprinklrService:

    def __init__(self, payload):
        self.payloadJson = payload
        self.cache = CacheOperations(self.payloadJson)

    def worker(self):
        # convert to Sprinklr Payload
        messageId = self.cache.get()
        haptikToSprinklrAdapter = HaptikToSprinklrAdapter.Adapter(
            self.payloadJson)
        sprinklrPayload = haptikToSprinklrAdapter.toSprinklrPayloadModel(
                     messageId)
        msgAcknowledgement = SprinklrService.sendMessage(
                    self, sprinklrPayload)
        return msgAcknowledgement.status_code
