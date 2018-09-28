#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time


class auth():
    def __init__(self):
        self.token = ''
        self.devices_id = ''
        self.host = "localhost:8090"
        self.api_url = "http://localhost:8090/TotalControl/v1/"
        self.username = "sigma"
        self.password = "514B3673"

    #授权访问
    def login(self):
        """
        :return: dict {
                        "status": true,
                        "value": {
                            "token": "270eq7lXQK8bXYsJ"
                    }
                }
        """
        request_url = self.api_url + "login"
        conn = httplib.HTTPConnection(self.host)
        key = base64.b64encode(self.username+":"+self.password.encode("UTF-8"))
        header = {'Authorization': key}
        conn.request(method="GET", url=request_url, headers=header)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        self.token = resp['value']['token']
        return self.token


if __name__ == "__main__":
    token = {"token":"1212121"}
    a = {'q': 'all'}
    payload = dict(a, **token)
    print payload