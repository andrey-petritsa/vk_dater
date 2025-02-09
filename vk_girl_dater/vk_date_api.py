import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


class VkDateApi:
    def get_history(self):
        # URL для запроса
        url = "https://dating.vk.com/api/messenger.getHistory"

        # Поля формы для отправки (все значения передаются как строки)
        fields = {
            "user_id": "39277097",
            "limit": "25",
            "offset": "0",
            "_token": "4OH9Klxt-jHXg6W8qeYhtDWdtLHkoCnNCPIxzu6_XApjJpFAQ7bNnWX9iusAqglK_ib6nGXhknQfyHZWjgBi0MNYsPonkcUJMf9pSMgET4NNHwm1h4tbWTznoXCJDuiMb9lXiq9LwMNLCOUx0z2G3EsVzKRWou-VInUPxJXYxBsDyNdRVmf_V1hlxWy-xJX9f_dHQb5x6w9PT_RdTtZ1pMbgA227We20nFwEoeRvPE4",
            "_agent": "love1 version:1.1.0 build:42 commit:86f7253249 env:production platform:desktop_web client:0.0/web/none lang:ru tz:10800 vkid:179377912 screen:d/795x709/1.100000023841858",
            "_session": "179377912_1739035613555",
            "_v": "1.13",
        }

        # Создаем объект MultipartEncoder с заданной границей
        multipart_data = MultipartEncoder(
            fields=fields,
            boundary="----WebKitFormBoundary1R9RTgZGf7Cm5KWr"
        )

        # Заголовки запроса
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": multipart_data.content_type,
            # Формат: multipart/form-data; boundary=----WebKitFormBoundary1R9RTgZGf7Cm5KWr
            "origin": "https://prod-app7058363-83077aee15b7.pages-ac.vk-apps.com",
            "priority": "u=1, i",
            "referer": "https://prod-app7058363-83077aee15b7.pages-ac.vk-apps.com/",
            "sec-ch-ua": '"Opera GX";v="116", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0 (Edition Yx GX)"
            ),
        }

        # Отправляем POST-запрос
        response = requests.post(url, headers=headers, data=multipart_data)

        # Возвращаем ответ сервера в формате json
        jsn = json.loads(response.text)
        return jsn