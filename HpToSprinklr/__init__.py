import logging

import azure.functions as func

import redis



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    myHostname = "HpAdapter.redis.cache.windows.net"
    myPassword = "UnarcoKKeaKWbmxsAo8piLjp4sp9sJtEuw3UFTDoiHo="

    r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        phoneNumber = r.get(name)
        if phoneNumber:
            return func.HttpResponse(f"Hello, {name}. we found your phoneNumber {phoneNumber.decode('utf-8')}.")
        else:
            return func.HttpResponse(f"Hello, {name}. No entry with your name.")
    else:
        return func.HttpResponse(
             "we received your blank message",
             status_code=200
        )
