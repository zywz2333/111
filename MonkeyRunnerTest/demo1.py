# -*- coding: UTF-8 -*-

# 导入
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# 连接设备，手机的操作对象device
device = MonkeyRunner.waitForConnection()

# 启动软件
runComponent = "com.sunrise.scmbhc/.ui.activity.home.HomeActivity"
device.startActivity(component=runComponent)

# 提示框
#MonkeyRunner.alert("helloword!")

# 选择框
#MonkeyRunner.choice("a u ok", ["yes", "no"])

# 点击屏幕的坐标
time.sleep(3)
device.touch(943, 1850, MonkeyDevice.DOWN_AND_UP)
time.sleep(3)
device.touch(295, 332, MonkeyDevice.DOWN_AND_UP)

# 输入字符串
#time.sleep(3)
#device.touch(526, 720, MonkeyDevice.DOWN_AND_UP)
#time.sleep(3)
#device.type("13000000000")
time.sleep(3)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)

# 截图
time.sleep(3)
img_path = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\MonkeyRunnerTest\\test.png"
device.takeSnapshot().writeToFile(img_path, "png")