from ..Data.cacheOperations import CacheOperations
from ..Adapters import SprinklrToHaptikAdapter
from ..Services.HaptikService import HaptikService
import os
import logging


class SprinklrToHaptikService:

    def __init__(self, payload):
        self.payloadJson = payload
        self.cache = CacheOperations(self.payloadJson)

    def worker(self):
        # x=self.payloadJson.get("receiverProfile")
        # print(x["channelId)
        haptikService = HaptikService()
        receivedProfile = self.payloadJson.get(
            os.environ["haptik_received_profile"])
        channelId = receivedProfile[os.environ["haptik_channel_id"]]
        if channelId == os.environ["star_hub"]:
            logging.info("Channel Id is of StarHub")
            return 200
        else:
            sprinklrToHaptikAdapter = SprinklrToHaptikAdapter.Adapter(
                self.payloadJson)
            if self.cache.checkIfExists():
                logging.info("Existing user")
                # threadControl = haptikService.getThreadControl(self)
                # if threadControl == constants.HAPTIK:
                if(self.cache.getThreadControl() == "haptik"):
                    logging.info("Thread Control is with haptik")
                    # convert to Haptik Payloadww
                    haptikPayload = (
                        sprinklrToHaptikAdapter.toHaptikPayloadModel())
                    self.cache.updateValidityByMins(8)
                    msgAcknowledgement = haptikService.sendMessage(
                        haptikPayload)
                    return msgAcknowledgement.status_code

                else:
                    logging.info("Thread Control is with Sprinklr")
                    status = self.cache.updateValidityByDays(1)
                    return 200 if status else 400

            else:
                logging.info("User is coming for first time.")
                haptikModel = sprinklrToHaptikAdapter.toHaptikCreateUserModel()
                response = haptikService.createUser(haptikModel)
                if response.status_code == 200:
                    if self.cache.setThreadControl():
                        status = self.cache.insert()
                    else:
                        return 400
                    if status:
                        haptikPayload = (
                            sprinklrToHaptikAdapter.toHaptikPayloadModel())
                        msgAcknowledgement = haptikService.sendMessage(
                            haptikPayload)
                        return msgAcknowledgement.status_code
                    else:
                        return 400
                return 400
