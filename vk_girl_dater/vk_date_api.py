import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


class VkDateApi:
    def __init__(self):
        self.url = ""
        self.fields = {}
        self.multipart_data = None
        self.headers = {}
        self.token = None

    def make_get_hisory_url(self):
        self.url = "https://dating.vk.com/api/messenger.getHistory"

    def make_get_history_fields(self, user_id):
        self.fields = {
            "user_id": user_id,
            "limit": "25",
            "offset": "0",
            "_token":self.token,
            "_agent": "love1 version:1.1.0 build:42 commit:86f7253249 env:production platform:desktop_web client:0.0/web/none lang:ru tz:10800 vkid:179377912 screen:d/795x709/1.100000023841858",
            "_session": "179377912_1739035613555",
            "_v": "1.13",
        }

    def make_get_history_data(self):
        self.multipart_data = MultipartEncoder(
            fields=self.fields,
            boundary="----WebKitFormBoundary1R9RTgZGf7Cm5KWr"
        )

    def make_get_history_headers(self):
        self.headers = {
            "content-type": self.multipart_data.content_type,
        }

    def get_history(self, user_id):
        self.make_get_hisory_url()
        self.make_get_history_fields(user_id)
        self.make_get_history_data()
        self.make_get_history_headers()

        response = requests.post(self.url, headers=self.headers, data=self.multipart_data)

        jsn = json.loads(response.text)
        return jsn

    def send_message(self, message):
        r = self.__make_send_message_request(message)
        self.__send_send_message_request(r)

    def __make_send_message_request(self, message):
        fields = {
            "user_id": message['user_id'],
            "text": message['text'],
            "_token": self.token,
            "_v": "1.13",
        }

        return {
            'url':"https://dating.vk.com/api/messenger.send",
            'headers':{"content-type":MultipartEncoder(fields=fields, boundary="----WebKitFormBoundaryVCgv4x0LhAoyptwt").content_type},
            'data':MultipartEncoder(fields=fields, boundary="----WebKitFormBoundaryVCgv4x0LhAoyptwt")
        }

    def __send_send_message_request(self, r):
        response = requests.post(r['url'], headers=r['headers'], data=r['data'])
        if not response.ok:
            raise Exception(response.text + str(response.status_code))

    def make_get_chats_url(self):
        self.url = "https://dating.vk.com/api/messenger.getChats"

    def make_get_chats_fields(self):
        self.fields = {
            "limit": "24",
            "offset": "0",
            "filter": "chat",
            "_token": self.token,
            "_agent": "love1 version:1.1.0 build:45 commit:b56925d360 env:production platform:desktop_web client:0.0/web/none lang:ru tz:10800 vkid:179377912 screen:d/795x709/1.100000023841858",
            "_session": "179377912_1740251026686",
            "_v": "1.13",
        }

    def make_get_chats_data(self):
        self.multipart_data = MultipartEncoder(
            fields=self.fields,
            boundary="----WebKitFormBoundary8fenChiD4DILfGM4"
        )

    def make_get_chats_headers(self):
        self.headers = {
            "content-type": self.multipart_data.content_type
        }

    def get_chats(self):
        self.make_get_chats_url()
        self.make_get_chats_fields()
        self.make_get_chats_data()
        self.make_get_chats_headers()
        response = requests.post(self.url, headers=self.headers, data=self.multipart_data)

        return response.text
