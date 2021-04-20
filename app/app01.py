import pytest
from appium import webdriver
import hamcrest

class TestDW():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.main.view.MainActivity'
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

    @pytest.mark.parametrize(
        'send_key, expect_price', [
            ("阿里巴巴", 180), ("小米概念",1210)
        ]
    )
    def test_app(self, send_key, expect_price):
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(send_key)
        self.driver.find_element_by_xpath(f'//*[@resource-id="com.xueqiu.android:id/name"and@text="{send_key}"]').click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert hamcrest.close_to(current_price, expect_price*0.1)

    @pytest.mark.skip
    def test_login(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号或邮箱")').send_keys("18109151750")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("ly199811000")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()


if __name__ == '__main__':
    pytest.main()