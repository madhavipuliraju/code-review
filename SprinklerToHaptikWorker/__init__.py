import logging
import azure.functions as func
from .Services.SprinklrToHaptik import SprinklrToHaptikService


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(
        'Python HTTP trigger function processing SprinklrToHaptik request.')
    statusCode = 200
    try:
        req_body = req.get_json()
    except ValueError:
        message = 'No valid Json attached'
    else:
        event_name = str(req_body.get("type"))
        if event_name == "message.created":
            adapter = SprinklrToHaptikService(req_body)
            statusCode = adapter.worker()
            message = (
                'This HTTP triggered function executed successfully.'
                + ' Event name: ' + event_name + ". Status code: "
                + str(statusCode))
            logging.info(statusCode)
        else:
            message = (
                "Not a message create event."
                + " HTTP triggered function executed successfully."
                + " Event name: " + event_name)

    return func.HttpResponse(
         message,
         status_code=statusCode
    )
