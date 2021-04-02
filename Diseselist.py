import requests
import bs4
from bs4 import BeautifulSoup
youlai="https://www.youlai.cn"
url="https://www.youlai.cn/dise/pz_B_1.html"

def findqapage(url):
    page = requests.get(url)
    # 输出200代表成功访问
    if page.status_code != 200:
        return None

    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('html')
    body = soup.find('body')
    m = list(body.children)[11]
    me = m.find('div')
    men = me.find('ul')
    for id, item in enumerate(list(men.children)):
        if id % 2 == 1:
            title = item.find('a')
            if title.get_text() == '相关问答':
                print(youlai + title['href'])  # 问答列表url
                return youlai + title['href']

page=requests.get(url)
#输出200代表成功访问
print(page.status_code)

soup = BeautifulSoup(page.content,'html.parser')
#此处html也是一个bs对象
html=soup.find('html')
#head=list(html.children)[1]
body=list(html.children)[3]
mbody=list(body.children)[11]
mabody=mbody.find('div')
alp=mabody.find('dl')#字母表导航栏

d=list(mabody.children)[9]
di=list(d.children)[3]
dis=di.find('div')
diss=dis.find('dl')
for id, item in enumerate(list(diss.children)):
    if id%2==1:
        for i in list(item.children):
            print(type(i))
        for idi, i in enumerate(list(item.children)):
            if idi%2==1:
                if i.name == 'a':
                    print(youlai+i['href'])
                    QAlist_url=findqapage(youlai+i['href'])
                    if QAlist_url:
                        调用qalist





