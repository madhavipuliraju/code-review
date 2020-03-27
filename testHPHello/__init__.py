import logging
import azure.functions as func
from . import testRedis

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info('clients:' + testRedis.clientList )

    name = req.params.get('name')
    phoneNumber = req.params.get('phonenumber')
    phoneNumber = phoneNumber

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            phoneNumber = req_body.get('phonenumber')

    if name:
        if not testRedis.r.exists(name):
            if phoneNumber:
                testRedis.r.set(name,phoneNumber.encode('utf-8'))
                logging.info('successfully entered into cache')
                return func.HttpResponse(f'Hello, {name}. We got your number: {phoneNumber}.Successfully created entry into cache')
            else:
                return func.HttpResponse(f'Hello, {name}. No data to cache')
        else:
            return func.HttpResponse(f'Hello, {name}. Entry exists in cache')
    else:
        return func.HttpResponse(
             'Pass a name in the query string or in the request body.',
             status_code=200
        )
