from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:

    def setup(self):
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noRest": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, '//*[@text="我的"]')))
        self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/rl_login"]/android.widget.TextView [2]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/rl_login"]/android.widget.TextView [2]').click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((MobileBy.ID, 'com.xueqiu.android:id/login_account')))
        self.driver.find_element_by_id('com.xueqiu.android:id/login_account').send_keys("18109151750")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((MobileBy.ID, 'com.xueqiu.android:id/login_password')))
        self.driver.find_element_by_id('com.xueqiu.android:id/login_password').send_keys("ly199811000")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((MobileBy.ID, 'com.xueqiu.android:id/button_next')))
        self.driver.find_element_by_id('com.xueqiu.android:id/button_next').click()

