import numpy as np

def perceptron(x,y):
    # x:input data e.g.x=[1,2,3]
    # y:expected result
    n = 0.01
    # n:step size
    x.append(1)
    x=np.array([x])
    x=x.T
    w=np.zeros([1,x.size])
    t=0
    while True:
        y2=w.dot(x)

        y2=y2[0,0]
        print(w)
        print(x)

        if abs(y2-y)>1e-9:
            w+=n*(y-y2)
            # print(w)
        else :
            break
    return w


if __name__=='__main__':
    print(perceptron([1,2,1],1))