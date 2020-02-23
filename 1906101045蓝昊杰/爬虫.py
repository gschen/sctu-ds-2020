import requests

from urllib import re

base_url = 'http://ns.meituan.com/meishi/b25710/'

cookies_str = ''

cookies_dict = {}
for cookie in cookies_str.split(";"):
    k, v = cookie.split("=", 1)
    cookies_dict[k.strip()] = v.strip()

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'
}

page = requests.get(
    url=base_url,
    cookies=cookies_dict,
    headers=headers
)

def get_element_from_html(raw_html):
    regex = ReUtil.get_regex(begin_with=['"poiInfos":'], end_with=['},"comHeader"'])
    result = regex.findall(raw_html)
    print(result[0][1])
    ans = ""
    for i in range(4):
        ans += result[0][i]
    return result

get_element_from_html(page.text)