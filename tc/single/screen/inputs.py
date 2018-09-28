#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_screen_inputs(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def screen_inputs_click(self, x, y, state="press"):
        """
        发送点击事件，对坐标 (x, y) 进行点击操作(按下/弹起/滑动/点击)
        :param devices_id:
        :param x:x 坐标
        :param y:	y 坐标
        :param state:状态值（缺省press）-down 按下-up 弹起-move 移动-press 点击(按下+弹起)
        :return:{"status":true}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/inputs"
        conn = httplib.HTTPConnection(self.host)
        body = {'x': x, 'y': y, 'token': self.token,"state":state}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def screen_inputs_send(self, code, state="press"):
        """
        发送一个手机按键事件，如 home、menu、back 等，可以实现按键的按下、弹起事件，或者直接发送点击事件（按下+ 弹起）完成点击动作
        :param devices_id:
        :param code: 键码值
            -menu  菜单键
            -home  home键
            -back  后退键
            -space 空格键
            -backspace 退格键
            -enter 回车键
            -up    向上动作
            -power 电源键
            -recentapp 最近应用功能键
            -down  向下动作
            -left  向左动作
            -right 向右动作
            -up   ?
        :param state:状态值（缺省press）
            -down 按下
            -up 弹起
            -move 移动
            -press 点击(按下+弹起)
        :return: {"status":true} 操作成功/失败
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/inputs"
        conn = httplib.HTTPConnection(self.host)
        body = {'code': code,'token': self.token, "state": state}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def screen_inputs_shift(self, direction):
        """
        操作设备进行方向滑动操作
        :param devices_id:
        :param direction: 滑动方向
                -up
                -down
                -left
                -right
        :return: {"status":true} 操作成功/失败
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/inputs"
        conn = httplib.HTTPConnection(self.host)
        body = {'direction': direction, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def screen_inputs_swipe(self, coord):
        """
        模拟用户操作的触控事件，可以实现单点或者多点操作的滑动事件。 坐标格式：在数组中的第一个坐标组为按下坐标；
        在数组中的最后一个坐标组为弹起坐标；中间数组为滑动坐标
        :param devices_id:
        :param coord: 滑动路线坐标集 [[124,256,30],[224,296,100],[324,356,1]]
        :return:  {"status":true} 操作成功/失败
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/inputs"
        conn = httplib.HTTPConnection(self.host)
        body = {'coord': coord, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res
