#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ten-armed bandit simulation
#author:cy@cchenyuee@outlook.com

import numpy as np
import matplotlib.pyplot as plt

def pure_greedy(q,steps):
    max_q=max(q)
    cal=[0]
    avg=[0]
    for i in range(steps-1):
        R=np.random.normal(loc=max_q,scale=1)
        cal.append(R)
        avg.append(np.mean(cal))
    return avg
def epsilon_greedy(q,epsilon,steps):
    max_q = max(q)
    cal = [0]
    avg = [0]
    for i in range(steps-1):
        bound = np.random.uniform()
        if bound>=epsilon:
            random_q=np.random.randint(low=0,high=10)
            R=np.random.normal(loc=random_q,scale=1)
        else:
            R = np.random.normal(loc=max_q, scale=1)
        cal.append(R)
        avg.append(np.mean(cal))
    return avg


q = np.random.normal(loc=0, scale=1, size=[10])
R1=pure_greedy(q,1000)
R2=epsilon_greedy(q,0.1,1000)
R3=epsilon_greedy(q,0.01,1000)
plt.plot([i for i in range(1000)],R1,color='red')
plt.plot([i for i in range(1000)],R2,color='green')
plt.plot([i for i in range(1000)],R3,color='black')
plt.show()