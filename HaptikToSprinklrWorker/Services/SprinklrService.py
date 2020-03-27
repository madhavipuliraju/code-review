import requests
import os


class SprinklrService:

    def sendMessage(self, payload):
        json1 = payload.__dict__
        response = requests.post(
            os.environ["sprinklr_url"], json=json1, headers={
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'Authorization': os.environ["sprinklr_authorization"],
                'Key': os.environ["sprinklr_key"]})
        return response
