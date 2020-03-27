import logging
import azure.functions as func
from .Services.SprinklrToHaptik import SprinklrToHaptikService


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(
        'Python HTTP trigger function processing SprinklrToHaptik request.')
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        adapter = SprinklrToHaptikService(req_body)
        statusCode = adapter.worker()

    return func.HttpResponse(
         "This HTTP triggered function executed successfully.",
         status_code=statusCode
    )
