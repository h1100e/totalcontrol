#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_script(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def script_run(self,file_name):
        request_url = self.api_url + "script"
        conn = httplib.HTTPConnection(self.host)
        body = {'file_name': file_name, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res
