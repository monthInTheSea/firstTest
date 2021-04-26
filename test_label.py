import allure
import requests


class TestLabel:

    def setup(self):
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        access_token = {
                "corpid": "ww21b61721c9ef5272",
                "corpsecret": "dHcc2iAcvnwqT1vxhYfnGWELLEG8Cw_3PEzQUZp-duc"
            }

        req = requests.get(url=url, params=access_token)
        self.token = req.json()['access_token']

    @allure.story('test_create')
    def test_create_label(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data ={
                "tagname": "label",
                "tagid": 12
            }
        req = requests.post(url=url, json=data)
        assert req.json()['errcode'] == 0

    @allure.story('test_update')
    def test_update_label_name(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
             "tagid": 12,
             "tagname": "放假提醒"
        }
        req = requests.post(url=url, json=data)
        assert req.json()['errcode'] == 0

    @allure.story('test_delete')
    def test_delete_label(self):
        tad_id = 12
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tad_id}"
        req = requests.get(url=url)
        assert req.json()['errcode'] == 0