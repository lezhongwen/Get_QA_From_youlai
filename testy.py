import requests
import bs4
import numpy as np
from bs4 import BeautifulSoup

youlai = "https://www.youlai.cn"

#准备用于存储数据的npy对象
global QAL, QDAL
QAL = np.empty(dtype=str, shape=[0, 2])
QDAL=np.empty(dtype=str, shape=[0, 3])

def QAlist(url):
    global QAL, QDAL
    page = requests.get(url)
    # 输出200代表成功访问
    print(page.status_code)
    if page.status_code != 200:
        return

    soup = BeautifulSoup(page.content, 'html.parser')
    # 此处html也是一个bs对象
    html = soup.find('html')
    #head = list(html.children)[1]
    body = list(html.children)[3]

    q = list(body.children)[18]  # 页面主题
    qu = list(q.children)[3]  # 问题大列表
    que = list(qu.children)[1]  # 问题小列表
    p = list(qu.children)[3]  # 翻页栏
    pa = list(p.children)[1]
    pag = list(pa.children)[1]

    for id, item in enumerate(list(que.children)):
        if (id % 2 == 1):
            # print(type(item))
            ques = list(item.children)[1]
            quest = list(ques.children)[0]
            print(youlai + quest['href'])  # 问答页入口
            QApage(youlai + quest['href'])

    for id, item in enumerate(list(pag.children)):
        if (hasattr(item, 'children')):
            page = list(item.children)[0]
            if (page.get_text() == "下一页"):
                print(youlai + page['href'])  # 递归到下一页

                QAlist(youlai + page['href'])

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

    body = list(html.children)[3]
    q = list(body.children)[17]
    qu = list(q.children)[3]  # 这里是问题和回答在一起

    que = list(qu.children)[3]  # 这里是问题和问题描述在一起

    ques = list(que.children)[1]
    quest = list(ques.children)[1]
    questi = list(quest.children)[1]
    print("问题：" + questi)  # 这里是问题了
    Q = questi

    quem = list(que.children)[3]
    quemi = list(quem.children)[4]
    print("详细描述：" + quemi.get_text())  # 这里是问题描述了
    QD = quemi.get_text()

    a = list(qu.children)[9]
    an = list(a.children)[3]
    ans = list(an.children)[1]
    print("回答：" + ans.get_text())  # 这里是回答
    A = ans.get_text()

    QAL = np.append(QAL, [[Q, A]], axis=0)
    QDAL = np.append(QDAL, [[Q, QD, A]], axis=0)


if __name__=="__main__":
    url="https://www.youlai.cn/dise/asklist/937_1.html"
    QAlist(url)
    print("问答对（不含病情详细描述）：")
    print(QAL)
    print("问答对（包含病情详细描述）：")
    print(QDAL)