class SprinklrPayloadModel:
    def __init__(self, payloadJson, messageId):
        self.accountId = 0
        x = payloadJson.get("message")
        self.content = {"text":  x["body"]["text"]}
        self.scheduleDate = 0
        self.taxonomy = {"campaignId": "testCampaignId"}
        self.inReplyToMessageId = messageId
