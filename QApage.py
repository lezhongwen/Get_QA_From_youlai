import requests
import bs4
import numpy as np
from bs4 import BeautifulSoup


url="https://www.youlai.cn/ask/749259.html"
page=requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

html=list(soup.children)[2]
head=list(html.children)[1]

body=list(html.children)[3]
q=list(body.children)[17]
qu=list(q.children)[3]#这里是问题和回答在一起

que=list(qu.children)[3]#这里是问题和问题描述在一起

ques=list(que.children)[1]
quest=list(ques.children)[1]
questi=list(quest.children)[1]
print("问题："+questi)#这里是问题了
Q=questi

quem=list(que.children)[3]
quemi=list(quem.children)[4]
print("详细描述："+quemi.get_text())#这里是问题描述了
QD=quemi.get_text()

a=list(qu.children)[9]
an=list(a.children)[3]
ans=list(an.children)[1]
print("回答："+ans.get_text())#这里是回答
A=ans.get_text()