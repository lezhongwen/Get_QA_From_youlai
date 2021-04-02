import numpy as np
QAL = np.empty(dtype=str, shape=[0, 2])

data = np.load('irqa_data.npy')
counter = 0

def KeyWordsCheck(Q):
    need = ['饮食', '饮用', '吃', '食', '伙食', '膳食', '喝', '菜' ,'忌口', '补品', '保健品', '食谱', '菜谱', '食用', '食物','补品']
    no = ['口吃']
    for item in no:
        if Q.find(item) != -1:
            return False
    for item in need:
        if Q.find(item) != -1:
            return True
    return False

for item in data:
    if KeyWordsCheck(item[0]):
        QAL = np.append(QAL, [item], axis=0)  # 存储问答对到QAL
        counter+=1

print(counter)
for item in QAL:
    print('Q:'+item[0])
    print('A:'+item[1]+''
                       '')

filename = 'cleaned_irqa_data.npy'
np.save(filename, QAL)