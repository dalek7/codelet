#-*- coding: utf-8 -*-
import numpy as np
np.random.seed(0)

p1 = np.random.choice(5, 10) # 반복해서 10개 선택
print(p1)

p2 = np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])  # 선택 확률을 다르게 해서 10개 선택
print(p2)

p = np.array([0.1, 0.0, 0.7, 0.2])
index = np.random.choice([0, 1, 2, 3], p = p.ravel())

print(index)

