'''
this file includes markov chain;markov Reward Process
@author:chenyue
@email:cchenyuee@outlook.com
'''
import numpy as np
import numpy.linalg as lg


class markov():
    def __init__(self,S,P,R,r):
        #S:origin condition; 1*n matrix
        # P:State transition matrix; n*n matrix
        # R:reward; 1*n matrix
        # r:Reward factor 1*n matrix
        self.S=S
        self.P=P
        self.R=R
        self.r=r
    def markov_chain(self,step):
        #this function calculate final state according to basic information and steps.
        a=S.dot(P)
        for i in range(step-1):
            a=a.dot(P)
        return a
    def markov_reward(self,chain):
        #chain is a set of all the conditions, e.g(1,2) represents from condition1 to condition2
        summary_reward=0
        for i in range(len(chain)):
            this_reward=R[0,i]
            this_reward*=(r[0,i])^i
            summary_reward+=this_reward
        return summary_reward
    def Bellmen_equation(self):
        #complexity: O(n^3)
        a=lg.inv(1-r*P)
        v=a.dot(R)
        return v

if __name__=='__main__':
  S=np.array([[0,1,0]])
  P=np.array([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]])
  R=np.array([[0,1,0]])
  r=np.array([[0,1,0]])
  m=markov(S,P,R,r)
  ans=m.markov_chain(3)
  print (ans)