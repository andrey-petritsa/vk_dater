import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


class VkDateApi:
    def __init__(self):
        self.url = ""
        self.fields = {}
        self.multipart_data = None
        self.headers = {}

    def make_get_hisory_url(self):
        self.url = "https://dating.vk.com/api/messenger.getHistory"

    def make_get_history_fields(self):
        self.fields = {
            "user_id": "39277097",
            "limit": "25",
            "offset": "0",
            "_token": "U7HKmybfkUgEGtyzxz4MYQRYzLPrIUdBYFGV7A57B_cq84I-jSdpdJ2koMAidtL57grtxbA9a_jMEMBYtK5jGNhP8nU4t0fzb4dpCxafJJs6EIipMyEbEKeF5Hrn5P7kElV_DoykSwJz2MsuKlfmgd68vBPsC6a2qbedU-9LMV7NFdVLR8xF_yt1fhsqk_uRM4HdyOcaP8-irCoZIDfcBam_BAHjo29mQpgUD9cF_dQ",
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

    def get_history(self):
        self.make_get_hisory_url()
        self.make_get_history_fields()
        self.make_get_history_data()
        self.make_get_history_headers()

        response = requests.post(self.url, headers=self.headers, data=self.multipart_data)

        jsn = json.loads(response.text)
        return jsn
