import requests
import bs4
import numpy as np
from bs4 import BeautifulSoup

youlai = "https://www.youlai.cn"

# 准备用于存储数据的npy对象
global QAL, QDAL
QAL = np.empty(dtype=str, shape=[0, 2])
#QDAL=np.empty(dtype=str, shape=[0, 3])

# 从疾病页面寻找的问答列表页面
def findqapage(url):
    page = requests.get(url)
    # 输出200代表成功访问
    if page.status_code != 200:
        return

    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('html')
    body = html.find('body')
    m = list(body.children)[11]
    me = m.find('div')
    men = me.find('ul')
    for id, item in enumerate(list(men.children)):
        if id % 2 == 1:
            title = item.find('a')
            if title.get_text() == '相关问答':
                print(youlai + title['href'])  # 输出问答列表的url
                return youlai + title['href']

# 遍历问答列表页面的所有问答页面
def QAlist(url):
    global QAL, QDAL
    page = requests.get(url)
    # 输出200代表成功访问
    print(page.status_code)
    if page.status_code != 200:
        return

    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('html')
    if (hasattr(html, 'children')):
        body = html.find('body')

        q = list(body.children)[18]  # 页面主题
        qu = list(q.children)[3]  # 问题大列表
        que = list(qu.children)[1]  # 问题小列表

        for id, item in enumerate(list(que.children)):
            if (id % 2 == 1):
                if (hasattr(item, 'children')):
                    ques = list(item.children)[1]
                    quest = list(ques.children)[0]
                    print(youlai + quest['href'])  # 输出问答页入口
                    QApage(youlai + quest['href'])

        p = list(qu.children)[3]  # 翻页栏
        pa = list(p.children)[1]
        if len(list(pa.children)) == 2:
            pag = list(pa.children)[1]
        else:
            return
        for id, item in enumerate(list(pag.children)):
            if (hasattr(item, 'children')):
                page = list(item.children)[0]
                if (page.get_text() == "下一页"):
                    print(youlai + page['href'])  # 递归到下一页
                    QAlist(youlai + page['href'])

# 问答页面信息爬取
def QApage(url):
    global QAL, QDAL
    page = requests.get(url)
    # 输出200代表成功访问
    print(page.status_code)
    if page.status_code != 200:
        return

    soup = BeautifulSoup(page.content, 'html.parser')

    html = soup.find('html')
    head = list(html.children)[1]

    body = html.find('body')
    q = list(body.children)[17]
    qu = list(q.children)[3]  # 页面主体

    que = list(qu.children)[3]  # 问题&问题描述

    ques = list(que.children)[1]
    quest = list(ques.children)[1]
    questi = list(quest.children)[1]
    print("问题：" + questi)  # 问题
    Q = questi

    '''quem = list(que.children)[3]
    quemi = list(quem.children)[4]
    print("详细描述：" + quemi.get_text())  # 问题描述
    QD = quemi.get_text()'''

    a = list(qu.children)[9]
    an = list(a.children)[3]
    ans = list(an.children)[1]
    print("回答：" + ans.get_text())  # 回答
    A = ans.get_text()

    QAL = np.append(QAL, [[Q, A]], axis=0)  # 存储问答对到QAL
    #QDAL = np.append(QDAL, [[Q, QD, A]], axis=0)

# 按照字母遍历所有疾病页面
def diseslist(url):
    page = requests.get(url)
    # 输出200代表成功访问
    if page.status_code != 200:
        return
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('html')
    body = html.find('body')
    mbody = list(body.children)[11]
    mabody = mbody.find('div')

    d = list(mabody.children)[9]
    di = list(d.children)[3]
    dis = di.find('div')
    diss = dis.find('dl')
    for id, item in enumerate(list(diss.children)):
        if id % 2 == 1:
            for i in list(item.children):
                print(type(i))
            for idi, i in enumerate(list(item.children)):
                if idi % 2 == 1:
                    if i.name == 'a':
                        print(youlai + i['href'])
                        QAlist_url = findqapage(youlai + i['href'])
                        if QAlist_url:
                            QAlist(QAlist_url)

if __name__=="__main__":
    url = "https://www.youlai.cn/dise/pz_A_1.html"
    page = requests.get(url)
    # 输出200代表成功访问
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('html')
    body = html.find('body')
    mbody = list(body.children)[11]
    mabody = mbody.find('div')
    alp = mabody.find('dl')  # 字母表导航栏
    alph = alp.find('dd').find('p')
    for item in list(alph.children):
        if item.name == 'a':
            print(youlai + item['href'])
            diseslist(youlai + item['href'])
    '''print("问答对（不含病情详细描述）：")
    print(QAL)
    print("问答对（包含病情详细描述）：")
    print(QDAL)'''
    filename = 'irqa_data.npy'
    np.save(filename, QAL)