'''
this file is classification by perceptron
@author:chenyue
@email:cchenyuee@outlook.com
'''

import numpy as np

def classify(x):
    # x is data to be classified, e.g.[[[1,1],1],[[1,2],0]]
    # output the solution vector
    x0=x[0]
    w=np.zeros([1,len(x0[0])+1])
    for i in x:
        if i[1]==0:
            i[0]=[-j for j in i[0]]
            i[0].append(-1)
        else:
            i[0].append(1)
    # pretreatment, augmentation and normalization
    while True:
         vector=[]
         for i in x:
            t=[j for j in i[0]]
            t=np.array([t])
            t_reserve=t.T
            if w.dot(t_reserve) <=0 :
                w+=t
                vector.append(0)
         if 0 not in vector:
             return w[0]
             break

if __name__=='__main__':
    print(classify([[[0,0],1],[[0,1],1],[[1,0],0],[[1,1],0]]))