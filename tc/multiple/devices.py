#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth

class multiple_devices(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    # 获取多个设备的id
    def get_devices(self):
        """
        获取多个设备的id ，地址是同一个，用户名密码是同一个，token 是同一个，如果连接到的多个设备，可以通过以下方法获取
        :param token: 授权访问token
        :return: dict {'ids': ['device@1770543457', 'device@-230441652']}
        """
        # token = {"token": token,"q":"all"}
        request_url = self.api_url + "devices/main?token=" + self.token + "&q=all"
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def get_devices_by_group(self,group_name):
        """
        根据group name 获取当前组下所有的设备id
        :param group_name: 组名
        :return: dict {'ids': ['device@1770543457', 'device@-230441652']}
        """
        request_url = self.api_url + "devices?q=group&name="+group_name+"&token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        """
        {
            "id":"device@1116106541"
        }
        """
        # main = resp['id']
        return resp

    def get_devices_by_name(self,name):
        """
        根据设备名得到设备id
        :param name: 设备名
        :return: {"id": "device@59007191"}
        """
        request_url = self.api_url + "devices?q=name&name=" + name + "&token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def connect_devices(self):
        """
        发起连接所有准备好的设备，不知是否支持多设备，接口描述前后矛盾
        :return:{"ids":["device@795844152","device@795812215"]}
        """
        request_url = self.api_url + "devices/connections?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def get_devices_properties(self, devices_ids):
        """
        根据设备id 获取设备属性
        :param devices_id: 设备id
        :return:
        {
            "status": true,                     boolean    true:成功; false:失败
            "value": {
                "name": "abcd3",                string    设备名称
                "IP": "",                       string    IP地址
                "IMEI": "A0000045722750",       string    IMEI 号
                "DPI": "480",                   string    屏幕的像素尺寸
                "SN": "0eb9448d",               string    唯一编号
                "width": 1080,                  string    屏幕分辨率宽度
                "height": 1920,                 string    屏幕分辨率高度
                "androidVersionRelease": "5.0", string    Android 版本
                "androidVersionSdkInt": 21,     string    Android SDK 版本
                "manufacturer": "samsung",      string    制造商名称
                "model": "SM-N9009",            string    型号
                "id": "device@1116106541",      string    ID值
                "colorbits": 32,                string    颜色位
                "orientation": 0,               string    屏幕方向，0：竖屏；1：横屏
                "sdcard": "/sdcard",            string    SDCARD 路径
                "tmp_path": "/data/local/tmp",  string    临时目录路径
                "acceleration": 1               string
            }
        }
        """
        request_url = self.api_url + "devices/ids?ids="+str(devices_ids)+"?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def devices_lock(self, lock, timeout):
        """
        锁定或解锁设备
        :param devices_id: 设备id
        :param lock: true/false true:锁定; false:解锁
        :param timeout: 锁定时间(毫秒)
        :return: {"status": true} true:成功; false:失败
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'lock': lock,'timeout': timeout, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def test(self):
        """
        操控多台设备执行相同的命令，devices 后面不再是 具体的设备id值，面是ids，在url参数里加上设备id的集合，
        格式为 ids=["device@1116106541", "device@1116106542"]
        :return:
        """
        # http://localhost:8090/TotalControl/v1/devices/ids/apps/com.sigma_rt.totalcontrol?
        # token=270eq7lXQK8bXYsJ&state=active&ids=["device@1116106541", "device@1116106542"]
        pass