#!/usr/bin/env python
# coding: utf-8

# In[4]:


from random import randint as rnd
import matplotlib.pyplot as plt

N = 100
length = 40
_list = [rnd(1, N) for i in range(length)]
print(_list)

for i in range(length-1):
    _min = i
    for j in range(i+1 , length):
        if _list[j]<_list[_min]:
            _min = j
    _list[i], _list[_min] = _list[_min], _list[i]
    plt.bar(list(range(length)), _list)
    plt.pause(0.005)
    plt.clf()
plt.show()
print(_list)


# In[ ]:




