import numpy as np
data = np.load('irqa_data.npy')
counter = 0
for item in data:
    print('Q:'+item[0])
    print('A:'+item[1]+''
                       '')
    counter+=1
print(counter)