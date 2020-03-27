import requests
import os
import logging


class HaptikService:

    def __init__(self):
        self.HEADERS = {
                'client-id': os.environ["haptik_client_id"],
                'Authorization': os.environ["haptik_authorization"]}

    def createUser(self, request):
        json1 = request.__dict__
        response = requests.post(
            os.environ["haptik_create_user_url"],
            json=json1, headers=self.HEADERS)
        logging.info(
            "Request made to Haptik created user API. Response status: "
            + str(response.status_code))
        return response

    def sendMessage(self, payload):
        jsonString = payload.__dict__
        logging.info("Message send request initiated to Haptik.")
        response = requests.post(
            os.environ["haptik_send_msg_url"],
            json=jsonString, headers=self.HEADERS)
        logging.info("Response status: " + str(response.status_code))
        return response
