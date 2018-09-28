#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_screen_images(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def screen_shot(self, filetype, filepath=None, rect=None, location=None):
        """
        截图
        :param deviceId: 设备id (必选)
        :param token: 授权访问token(必选)
        :param filepath: 截屏文件保存路径（截屏保存到手机必选）
        :param filetype: 截屏保存文件类型，值可以为：[bmp/png/jpg](必选)
        :param rect:     格式：[topLeftX,topLeftY,bottomRightX,bottomRightY] (非必选)
                        指定截屏区域，具体说明如下:
                        topLeftX： 屏幕上指定范围左上角 X 坐标
                        topLeftY： 屏幕上指定范围左上角 Y 坐标
                        bottomRightX： 屏幕上指定范围右下角 X 坐标
                        bottomRightY： 屏幕上指定范围右下角 Y 坐标
        :param location:截屏保存到设备或者PC: (非必选)
                        pc:保存到PC电脑
                        device:保存到移动设备
        :return: dict 截图保存到PC返回值：
                        {
                            "status": true,
                            "file_url": "http://localhost:8090/867924024124417/1523049073460.bmp"
                        }
                        截屏保存到设备返回值：
                        {
                            "status": true
                        }
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/images?token=" + self.token
        request_url = request_url + "&type=" + filetype
        if filepath:
            request_url = request_url + "&file=" + filepath
        if rect:
            request_url = request_url + "&rect=" + rect
        if location:
            request_url = request_url + "&location=" + location
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp

    def screen_seek_image(self,name,sim=None,rect=None,same=None,beGray='true'):
        """
        在全屏或指定区域范围内寻找指定图片的坐标，支持相似查找。如找到目标图，则返回找到位置的左上角坐标
        :param deviceId: 设备id  (必选)
        :param token: 授权访问token (必选)
        :param name: 需要对比图片路径（本地路径） (必选)
        :param sim: 相似度，取值范围为[0.0, 1.0]  (非必选) 必须和beGray 这个参数同时存在
        :param rect: 格式：[topLeftX,topLeftY,bottomRightX,bottomRightY]  (非必选)
                        指定截屏区域，具体说明如下:
                        topLeftX： 屏幕上指定范围左上角 X 坐标
                        topLeftY： 屏幕上指定范围左上角 Y 坐标
                        bottomRightX： 屏幕上指定范围右下角 X 坐标
                        bottomRightY： 屏幕上指定范围右下角 Y 坐标
        :param same: 当此值为true时，表示要寻找的小图和大图取自同一台手机，因此在找图时无需缩放，也无需进行相似查找。对于在同一台手机上的找图行为，这两个函数更加快速准确。Device.seekImage(imageName, sim, same) TC 6.8.0 之前可以使用

        :param beGray:当此值为true时(默认为true)，表示图片要先进行灰度处理，然后再进行找图。(非必选)
                        当此值为false时候，表示图片不进行任何处理就进行找图，当然灰度处理后找图速度更快。从 TC 6.8.0 开始可以使用。

        :return: dict {"status": true,"value":[272,371]}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/images?token=" + self.token
        request_url = request_url + "&name=" + str(name)
        if sim:
            request_url = request_url + "&sim=" + str(sim)
        if rect:
            request_url = request_url + "&rect=" + str(rect)
        if same:
            request_url = request_url + "&same=" + str(same)
        if beGray:
            request_url = request_url + "&beGray=" + str(beGray)
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp

    def screen_seek_image_by_id(self, id, sim=None):
        """
        根据 imageID 在手机屏幕上查找指定图像
        :param devices_id:
        :param id: 图像 ID
        :param sim:  相似度，取值范围为[0.0, 1.0]
        :return: dict {"status": true,"value":[272,371]}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/screen/images?token=" + self.token
        request_url = request_url + "&id=" + id
        if sim:
            request_url = request_url + "&sim=" + sim
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        resp = json.loads(res)
        print resp
        return resp
