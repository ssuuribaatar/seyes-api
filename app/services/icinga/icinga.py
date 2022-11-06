#!/usr/bin/env python

import requests
import json
from pprintpp import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


def create_connection_data(hostname, username, password, port=5665):
    disable_warnings(InsecureRequestWarning)
    request_url = f"https://{hostname}:{port}/v1/objects/services"
    headers = {
        'Accept': 'application/json',
        'X-HTTP-Method-Override': 'GET'
        }
    auth = (username, password)
    data = json.dumps({
        "attrs": ["name", "state"],
    })
    r = requests.get(request_url,
                     headers=headers,
                     auth=auth,
                     data=data,
                     verify=False)
    return r


username = 'root'
password = '86f524b7c36862ed'
hostname = 'icinga2'


r = create_connection_data(hostname, username, password)


if (r.status_code == 200):
    pprint((r.json()['results']))
else:
    print(r.text)
    r.raise_for_status()
