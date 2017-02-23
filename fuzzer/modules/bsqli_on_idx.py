from time import time
from json import dumps

from requests import get, exceptions

from urllib.parse import urlparse, parse_qs


def go(web_request):
    result = []

    o = urlparse(web_request['url'])
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    for k, v in query.items():
        tmp_value = v
        query[k] = 'sleep(2)'
        a1 = time()
        try:
            r = get(url, params=query, timeout=5)
        except exceptions.Timeout:
            pass
        a2 = time()
        if a2 - a1 >= 2:
            tmp = {}
            tmp['url'] = url
            # tmp['headers'] = r.request.headers.__str__
            tmp['body'] = query
            result.append(dumps(tmp))
        query[k] = tmp_value

    if len(result) >= 1:
        return result
    else:
        return []
