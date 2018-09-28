#!/user/bin/python
# -*- coding:utf-8 -*-
import httplib
import json
import base64
import time
import tc.auth


class single_app(tc.auth.auth):

    def __init__(self, devices_id, token):
        tc.auth.auth.__init__(self)
        self.devices_id = devices_id
        self.token = token

    def app_close(self, packageName, state="inactive"):
        """
        关闭指定包名的 app。
        :param state: 等于inactive,表示操作类型
        :param packageName: App 包名
        :return:{  "status": true,  "value": "make it inactive" }status	boolean	true:成功; false:失败 value	string	操作信息
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps/"+packageName
        conn = httplib.HTTPConnection(self.host)
        body = {'state':state, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def app_run(self, packageName, state="active"):
        """
        打开app
        :param packageName:
        :param state:
        :return:
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps/"+packageName
        conn = httplib.HTTPConnection(self.host)
        body = {'state': state, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def app_install(self, file_name):
        """
        安装apk到设备。
        :param devices_id:
        :param file_name: apk文件路径 C:/Users/S/Desktop/test.apk
        :return:{"status": true,"value": "install apk success."}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps"
        conn = httplib.HTTPConnection(self.host)
        body = {'file_name': file_name, 'token': self.token}
        body = json.dumps(body).encode(encoding='utf-8')
        conn.request(method="POST", url=request_url, body=body)
        response = conn.getresponse()
        res = response.read()
        print(res)
        return res

    def get_running_apps(self,q="foreground_app"):
        """
        获取当前运行的app包名 (getForegroundApp)
        :param devices_id:
        :param q: 等于foreground_app表示操作类型
        :return: {"status": true, "value":"com.sigma_rt.totalcontrol"}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps?token=" + self.token
        request_url = request_url + "&q="+q
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def get_installed_apps(self, q="installed_apk_list"):
        """

        :param devices_id:
        :param q: installed_apk_list
        :return:
        {
            "status": true,
            "value":"[com.lewa.systemclean, com.lewa.providers.location, com.android.defcontainer, com.tencent.mm, com.lewa.thememanager, cn.kuwo.player, com.lewa.netmgr.adjust, com.mediatek.voiceunlock,......]
        }
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps?token=" + self.token
        request_url = request_url + "&q="+q
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp

    def app_uninstall(self, packageName):
        """
        卸载指定包名apk
        :param devices_id:
        :param packageName:
        :return:{"status": true}
        """
        request_url = self.api_url + "devices/" + self.devices_id + "/apps/"+packageName+"?token=" + self.token
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="DELETE", url=request_url)
        response = conn.getresponse()
        res = response.read()
        # print res
        resp = json.loads(res)
        return resp