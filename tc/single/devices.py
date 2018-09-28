#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_devices(tc.auth.auth):

    def __init__(self, token):
        tc.auth.auth.__init__(self)
        self.token = token

    # 获取设备id
    def get_devices_id(self):
        """

        :param token:  授权访问token(必选)
        :return: string 设备id
        """
        request_url = self.api_url + "devices/main?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        # header = {'Authorization': 'c2lnbWE6amllaHVh'}
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
        self.devices_id = resp['id']
        return resp['id']

    def get_devices_properties(self):
        """
        根据设备id 获取设备属性
        # :param devices_id: 设备id
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
        request_url = self.api_url + "devices/" + self.devices_id + "?token=" + self.token
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
        # :param devices_id: 设备id
        :param lock: true/false true:锁定; false:解锁
        :param timeout: 锁定时间(毫秒)
        :return: {"status": true} true:成功; false:失败
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'lock': lock, 'timeout': timeout, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def devices_modify_name(self, name):
        """
        更改设备名称
        :param devices_id: 设备id
        :param name: 要更改成的名称
        :return: {"status": true} true:成功; false:失败
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'name': name, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def devices_modify_vol(self, vol, volumes):
        """
        更改设备音量
        :param devices_id:
        :param vol: 常量值，需要调整的音量类型可为： VolRing（响铃音量） VolNotify（通知音量） VolMedia（媒体音量） VolAlarm（闹钟音量）
        :param volumes: 整型，0-100。音量的百分数大小
        :return: {"status": true} true:成功; false:失败
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'vol': vol, 'volumes': volumes, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def devices_exec_command(self, commandline, timeout):
        """
        执行命令 在设备 shell 控制台上同步调用的方式执行命令。同步调用是指可以在较短时间内执行完毕并且不需要用户交互的命令执行方式，如 ls，pwd 等。
        :param devices_id:
        :param commandline: 需要执行的命令
        :param timeout: 超时时间（毫秒）
        :return:status	boolean	true:成功; false:失败  value	string	返回数据
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'commandline': commandline, 'timeout': timeout, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def devices_send_message(self, phone_number, message):
        """
        向指定号码发送信息
        :param devices_id:
        :param phone_number: 号码
        :param message: 信息内容
        :return: {"status": true} true:成功; false:失败
        """
        request_url = self.api_url + "devices/" + self.devices_id
        conn = httplib.HTTPConnection(self.host)
        body = {'phone_number': phone_number, 'message': message, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def get_devices_message(self, position, count):
        """
        获取设备上的短信
        :param devices_id:
        :param position: 位置，从第几条开始获取
        :param count:    条数，获取几条
        :return:
        单条：
        {
          "status": true,
          "value": {
            "address": "13558543941",
            "body": "TC获取短信内容接口使用说明",
            "date": "2017-03-31 04:32:07",
            "type": "2"
          }
        }

        //多条
        {
          "status": true,
          "value": [{
            "address": "13558543941",
            "body": "TC获取短信内容接口使用说明",
            "date": "2017-03-31 04:32:07",
            "type": "2"
          }, {
            "address": "13668543941",
            "body": "欢迎使用TC。",
            "date": "2017-03-31 05:47:03",
            "type": "2"
          }]
        }
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/messages?token=" + self.token
        request_url = request_url + "&position=" + str(position) + "&count=" + str(count)
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def get_devices_message_count(self):
        """
        获取手机短信数量
        :param devices_id:
        :return: {"status":true,"value":34} status :成功/失败 ,value 数量
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/messages?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def devices_setting(self):
        """
        不知道有什么鸟用，说明写的是设置属性，接口写的是获取属性
        :param devices_id:
        :return:
        {
            "status": true,
            "value": {
                "display_mode": 1,
                "display_quality": 2,
                "display_accl": 2,
                "display_hw_decode": "1",
                "display_resolution_mode": 2,
                "display_orientation": 1,
                "display_resolution": "1080*1920"
            }
        }

        字段	类型	描述
        status	boolean	true:成功; false:失败
        display_mode	int	显示模式： 1 – 表示显示模式是HA1;  2 – 表示显示模式是HA2; 3 – 表示显示模式是Comp;
        display_quality	int	显示质量： 1 – High; 2 – Medium; 3-Low;
        display_accl	int	加速模式，对应的返回值为： 1 – GDI; 2 – DirectX; 3 - OpenGL;
        display_hw_decode	int	是否使用硬件解码，对应的返回值为： 1 – Yes; 0 – No;
        display_resolution_mode	int	分辨率模式，对应的返回值为： 1 - 480p; 2 - 640p; 3 - 720p; 4 - 1080p;
        display_resolution	string	屏幕的宽和高。例如：{h: 1920, w:1080}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/settings?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp
