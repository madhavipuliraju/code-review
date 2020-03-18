import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    phoneNumber = req.params.get('phonenumber')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            phoneNumber = req_body.get('phonenumber')

    if name:
        return func.HttpResponse(f"Hello, {name}. We got your number: {phoneNumber}")
    else:
        return func.HttpResponse(
             "Pass a name in the query string or in the request body.",
             status_code=200
        )
