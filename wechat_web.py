from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebWX:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_web_addresslist(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_link_text("通讯录").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_add_member:nth-child(2)')))
        while True:
            self.driver.find_element_by_css_selector(".js_add_member:nth-child(2)").click()
            element = self.driver.find_elements_by_id('username')
            if len(element) > 0:
                break
        self.driver.find_element_by_id('username').send_keys("alex")
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('1231456')
        self.driver.find_element_by_xpath('//*[@name="gender"and @value="1"]').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys("12446239999")
        self.driver.find_element_by_link_text("保存").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')))
        name_list = []
        list = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        for ele in list:
            name_list.append(ele.get_attribute("title"))
        assert "alex" in name_list
