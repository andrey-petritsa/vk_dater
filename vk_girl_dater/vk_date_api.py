import json
import subprocess

class VkDateApi:
    def get_history(self):
        curl_command = [
            'curl',
            'https://dating.vk.com/api/messenger.getHistory',
            '-H', 'content-type: multipart/form-data; boundary=----WebKitFormBoundaryAfLUEABv78B68huv',
            '--data-raw', self.build_get_history_request()
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def build_get_history_request(self):
        return '''------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="user_id"\r
\r
1\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="limit"\r
\r
25\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="offset"\r
\r
0\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="_token"\r
\r
2k7NBEq0r7J14V_203hb0U1Oml4qWxI5xuDDffjWgl1YXABcD_JwJ19FjEQykg9eZxSvlTKKiaBig_rMmvEAYRImUJ4PWom0fjUDj6h05qa5KLzJdpDnU-HJBzPL0tTBiiOxyP5z2TBPmE8EmNfE9KzSbq4FVfNLyokH2c7wR8YJIdVt8g5WlKdeUIhb0RR9EV6dgbhqmFUjWurvp2_xGDEz04L6cruWm4ZZtnH0BV0\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="_agent"\r
\r
love1 version:1.1.0 build:39 commit:c1b9c3036c env:production platform:mobile_web client:0.0%2Fmobile-web%2Fnone lang:ru tz:10800 vkid:85209899 screen:m%2F483x552%2F1.25\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="_session"\r
\r
85209899_1738689527173\r
------WebKitFormBoundaryAfLUEABv78B68huv\r
Content-Disposition: form-data; name="_v"\r
\r
1.13\r
------WebKitFormBoundaryAfLUEABv78B68huv--\r
'''

