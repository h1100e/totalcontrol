#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_screen_texts(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def screen_texts_analyze(self, rect,lang, mode):
        """
        查找文字 解析手机屏幕上指定范围的文字，该函数依赖uploadTessData指定的traineddata文件。
        :param devices_id:
        :param rect: 屏幕搜索区域左上、右下坐标 [100,200,300,400]
        :param lang: 要搜索图像对应的语言 eng
        :param mode: 搜索模式  singleline
        :return:{"status":true, "value":"text"}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/texts?token=" + self.token
        request_url = request_url + "&rect=" + rect
        request_url = request_url + "&lang=" + lang
        request_url = request_url + "&mode=" + mode
        print request_url
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp

    def screen_texts_input(self, text):
        """
        在设备中对焦点输入框进行文字输入。
        :param devices_id:
        :param text:  要输入的文字
        :return:{"status":true}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/texts?token=" + self.token
        request_url = request_url + "&text=" + text
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp

    def screen_texts_clipboard(self, type):
        """
        获取当前手机剪贴板中的文字内容
        :param devices_id:
        :param type:  固定值：clipboard_text ,代表剪贴板内容
        :return: {"status":true,"value":"text"} value ： 剪贴板内容文本
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/texts?token=" + self.token
        request_url = request_url + "&type=" + type
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp