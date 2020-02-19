import requests
from bs4 import BeautifulSoup
import json

url = 'http://bj.meituan.com/'
url_shop = 'http://bj.meituan.com/shop/{}'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'DNT':'1',
    'Host':'bj.meituan.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://bj.meituan.com/shop/286725?acm=UwunyailsW15518532529028663069.286725.1&mtt=1.index%2Fdefault%2Fpoi.pz.1.j4cijrmg&cks=58899',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


# 得到所有的二级菜单url
def get_start_menu_links():
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    links = [link.find('div').find('div').find('dl').find('dt').find('a')['href'] for link in soup.find_all('div',class_='J-nav-item') ]
    return links


def get_shop_ids(url, headers=None):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    content_id = json.loads(soup.find('div', class_='J-scrollloader cf J-hub')['data-async-params'])
    return json.loads(content_id.get('data')).get('poiidList')


def main():
    start_menu_links = get_start_menu_links()
    for link in start_menu_links:
        for pageNum in range(4,5):
            category_url = link + '/all/page{}'.format(pageNum)
            for shop_id in get_shop_ids(category_url, headers=headers):
                html = requests.get(url_shop.format(shop_id), headers=headers).text
                soup = BeautifulSoup(html, 'lxml')
                shop_detail = soup.find('div', class_='summary biz-box fs-section cf')
                print("==================================pageNum %d  shop_id: %d===================================================" % (pageNum,shop_id ))
                try:
                    shop_detail.find('div', class_='fs-section__left').find('h2').find('span').text
                except:
                    continue
                print("名称：      " + shop_detail.find('div', class_='fs-section__left').find('h2').find('span').text)
                print("地址：      " + shop_detail.find('div', class_='fs-section__left').find('p', class_='under-title').find('span').text)
                print("联系方式：   " + shop_detail.find('div', class_='fs-section__left').find('p', class_='under-title').find_next_sibling().text)


if '__main__' == __name__:
    main()