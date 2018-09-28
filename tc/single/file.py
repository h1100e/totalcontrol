#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_file(tc.auth.auth):
    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def file_upload(self, type, file_path):
        """
        接口未清淅定义，尚不明确如何使用
        :param devices_id:
        :param type:image script apk
        :param file_path:
        :return:
        {
            "status": true,
            "file_url": "http://localhost:8090/TotalControl/v1/storage/images/1527558556026.bmp"
        }
        """
        request_url = self.api_url + "storage?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        body = {'file': type + "=@" + file_path}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res
