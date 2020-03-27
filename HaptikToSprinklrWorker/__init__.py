import logging
import azure.functions as func
from .Services.HaptikToSprinklr import HaptikToSprinklrService


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(
        'Python HTTP trigger function processing HaptikToSprinklr request.')
    message = ''
    statusCode = 200
    try:
        req_body = req.get_json()
    except ValueError:
        message = 'No valid Json attached'
    else:
        event_name = str(req_body.get("event_name"))
        if event_name == "message":
            adapter = HaptikToSprinklrService(req_body)
            statusCode = adapter.worker()
            message = (
                "This HTTP triggered function executed successfully."
                + " Event name: " + event_name + ". Status code: "
                + str(statusCode))
        else:
            message = (
                "Not a message event."
                + " HTTP triggered function executed successfully."
                + " Event name: " + event_name)

    return func.HttpResponse(message, status_code=statusCode)
