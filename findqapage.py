import requests
import bs4
from bs4 import BeautifulSoup
youlai="https://www.youlai.cn"
url="https://www.youlai.cn/dise/104.html"
page = requests.get(url)
# 输出200代表成功访问
'''if page.status_code != 200:
    return'''

soup = BeautifulSoup(page.content, 'html.parser')
html = soup.find('html')
body = soup.find('body')
m = list(body.children)[11]
me = m.find('div')
men = me.find('ul')
for id, item in enumerate(list(men.children)):
    if id % 2 == 1:
        print(item)
        title = item.find('a')
        if title.get_text() == '相关问答':
            print(youlai+title['href'])#问答列表url


