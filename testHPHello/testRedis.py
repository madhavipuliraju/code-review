import redis
import json

myHostname = "HpAdapter.redis.cache.windows.net"
myPassword = "UnarcoKKeaKWbmxsAo8piLjp4sp9sJtEuw3UFTDoiHo="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

pingResult = str(r.ping())

clientList = json.dumps(r.client_list())