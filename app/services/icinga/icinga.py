#!/usr/bin/env python
import requests
import json
from pprintpp import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


class Icinga:
    def __init__(self, username, password, hostname, port=5665):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    def create_connection_data(self):
        disable_warnings(InsecureRequestWarning)
        request_url = f"https://{self.hostname}:{self.port}/v1/objects/hosts"
        headers = {
            'Accept': 'application/json',
            'X-HTTP-Method-Override': 'GET'
        }
        auth = (self.username, self.password)
        data = json.dumps({
            "attrs": ["name", "state"],
        })

        r = requests.get(request_url,
                         headers=headers,
                         auth=auth,
                         data=data,
                         verify=False)
        result = r.json()['results']
        self.hosts = result
        return result

    def get_host_summary(self):
        self.host_count = len(self.hosts)
        return self.hosts
