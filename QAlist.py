import requests
import bs4
from bs4 import BeautifulSoup
youlai="https://www.youlai.cn"
url="https://www.youlai.cn/dise/asklist/1015_1.html"
page=requests.get(url)
#输出200代表成功访问
print(page.status_code)

soup = BeautifulSoup(page.content,'html.parser')
#此处html也是一个bs对象
html=soup.find('html')
for item in list(soup.children):
    print(type(item))
#head=list(html.children)[1]

if (hasattr(html, 'children')):
    body = list(html.children)[3]

    q = list(body.children)[18]  # 页面主题
    qu = list(q.children)[3]  # 问题大列表
    que = list(qu.children)[1]  # 问题小列表

    for id, item in enumerate(list(que.children)):
        if (id % 2 == 1):
            # print(type(item))
            ques = list(item.children)[1]
            quest = list(ques.children)[0]
            print(youlai + quest['href'])  # 问答页入口

    p = list(qu.children)[3]  # 翻页栏
    pa = list(p.children)[1]
    if len(list(pa.children)) == 2:
        pag = list(pa.children)[1]
        for id, item in enumerate(list(pag.children)):
            if (hasattr(item, 'children')):
                page = list(item.children)[0]
                if (page.get_text() == "下一页"):
                    print(youlai + page['href'])  # 递归到下一页