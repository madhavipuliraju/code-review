class HaptikUserCreateModel:
    def __init__(self, payloadJson):
        self.auth_id = payloadJson.get("id")
        x = payloadJson.get("senderProfile")
        self.auth_code = x["channelId"]
        x = payloadJson.get("receiverProfile")
        self.mobile_no = x["channelId"]
        self.email = x["name"]
        self.name = x["name"]
        self.language_code = payloadJson.get("language")
