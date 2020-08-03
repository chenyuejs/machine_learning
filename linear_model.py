'''
this file includes linear regression;log odds regression;linear discriminant analysis
@author:chenyue
@email:cchenyuee@outlook.com
'''
import numpy as np

def Least_squares(x,y):
        #x,y are Independent variable and dependent variable respectively
        #x,y are n vector eg. x=[1,2,3];y=[1,2,3]
        m=len(x)
        w1=0
        w2=0
        w3=0
        b=0
        average_x=np.mean(x)
        for i in range(m):
            w1+=y[i]*(x[i]-average_x)
            w2+=x[i]*x[i]
            w3+=x[i]
        w=w1/(w2-w3*w3/m)
        for i in range(m):
            b+=y[i]-w*x[i]
        return [w,b/m]

def Multiple_linear_regression(x,y):
    '''
    y=w0+w1x1+...+wnxn
    y=wTxi+b
    :param x: 
    [[x11,x12,x13……x1n,1]
     [x21,x22,x23……x2n,1]
     ……
     [xn1,xn2,xn3……xnn,1]]
     y=wx
    :return: w
    '''
    xt=x.T
    w=xt.dot(x)
    w=w.I
    w=w.dot(xt)
    w=w.dot(y)
    return  w

def


if __name__=='__main__':
    x=[1,2,3]
    y=[1,2,3]
    [a,b]=Least_squares(x,y)
    print (a)
    print (b)