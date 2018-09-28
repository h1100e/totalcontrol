#!/user/bin/python
# -*- coding:utf-8 -*-
import time
from PIL import Image
import pytesseract

from tc.single.devices import single_devices
from tc.single.app import single_app
from tc.single.screen.images import single_screen_images
from tc.single.screen.inputs import single_screen_inputs
from tc.single.screen.texts import single_screen_texts

# text=pytesseract.image_to_string(Image.open('D:/SERVER/wwwroot/totalcontrol/cr/static/8.png'),lang='chi_sim+eng',config="-psm 6")
# # text=pytesseract.image_to_string(Image.open('D:/SERVER/wwwroot/totalcontrol/cr/static/nu.png'))
# print(text)
# exit(11)
d = single_devices()
token = d.login()
devices_id = d.get_devices_id()
print token
print devices_id

app = single_app()
app.token = token
app.devices_id = devices_id
# print app.get_running_apps()
# print app.get_installed_apps()
#打开app
app_name = "com.supercell.clashroyale.mi"
print app.app_run(app_name)
print "打开app"

time.sleep(10)
#图像识别
# img = single_screen_images()
# img.devices_id = devices_id
# img.token = token
# print "找到任务按钮,成功率太低"
# mb_rect = "[topLeftX,topLeftY,bottomRightX,bottomRightY]"
# rect_res = img.screen_seek_image("D:/SERVER/wwwroot/totalcontrol/cr/static/task.bmp",same='true',sim=0.7,beGray="true")
# print rect_res
# rect = rect_res['value']
# print "任务按钮坐标"+str(rect)

# time.sleep(3)
#点击事件
inp = single_screen_inputs()
inp.devices_id = devices_id
inp.token = token
# print "发送点击事件"
# print rect[0],rect[1]
print "打开玩家资料："
print inp.screen_inputs_click(400,200)
time.sleep(3)
print "点击个人资料："
print inp.screen_inputs_click(200,400)
print "查找玩家编号："
tex = single_screen_texts()
tex.devices_id = devices_id
tex.token = token
no_rect = "[40,552,120,580]"
print tex.screen_texts_analyze(no_rect,"eng","singleline") #CHN_ENG
time.sleep(3)
print "关闭个人资料："
print inp.screen_inputs_click(1000,300)
print "获取金币数量："
gold_rect = "[460,20,670,75]"
print tex.screen_texts_analyze(gold_rect,"eng","singleline") #CHN_ENG

print "获取宝石数量："
da_rect = "[830,20,1000,75]"
print tex.screen_texts_analyze(da_rect,"eng","singleline") #CHN_ENG

