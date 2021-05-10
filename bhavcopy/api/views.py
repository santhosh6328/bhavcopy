import redis

import simplejson
from django.http import HttpResponse

r = redis.Redis()

def all_data(request):
    items = {}
    for key in r.keys("*"):
        items[key.decode("utf-8")] = r.get(key)
    return HttpResponse(simplejson.dumps(items), content_type="application/json")
