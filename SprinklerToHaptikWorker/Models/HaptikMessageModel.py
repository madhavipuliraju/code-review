class HaptikPayloadModel:
    def __init__(self, payloadJson):
        self.user = {"auth_id": payloadJson.get("id")}
        msg = payloadJson.get("content")
        msgString = msg["text"]
        self.message_body = msgString
        self.message_type = 0  # payloadJson.get("type")
        self.business_id = 10  # payloadJson.get(10)
