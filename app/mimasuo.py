import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestApp():

    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desire_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desire_caps['platformVersion'] = '6.0'
        # 在此会话之前不要重置应用状态
        desire_caps['noReset'] = 'True'
        # 在使用 adb 启动应用程序之前，不会停止测试中的应用的过程
        desire_caps['dontStopAppOnReset'] = 'True'
        # 跳过设备初始化
        desire_caps['skipDeviceInitialization'] = 'True'
        # 设置支持中文
        desire_caps['unicodeKeyboard'] = 'True'
        desire_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touchAction(self):
        action = TouchAction(self.driver)
        action.press(x=120, y=170).wait(200).move_to(x=300, y=170).wait(200).release().wait(200).perform()

if __name__ == '__main__':
    pytest.main()