# totalcontrol
手机控rest api python sdk
简单封装了一下手机控的restapi，试了一下它的图像定位和图片文字识别功能，发现这两个接口都是摆设，无奈之下用了一下tesseract，识别效果仍然不好。后来换一种思路，用totalcontrol做区域截图，把图像传给百度ocr做图像里的文字识别，效果还是不错的，准确率很高。
#目录说明
tc目录下是api的封装，cr下面是拿皇室战争做的测试
#后续
下一步尝试一下谷歌的ocr。代码还不完善，后续有时间进一步更新。
