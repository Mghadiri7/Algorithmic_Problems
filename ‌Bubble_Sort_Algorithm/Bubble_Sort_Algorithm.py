from random import randint as rnd
import matplotlib.pyplot as plt
N = 100
length = 20
_list = [rnd(1,N) for i in range(length)]
print(_list)
counter = 0
for i in range(length-1):
    flag = False
    for j in range(length-i-1):
        if _list[j]>_list[j+1]:
            _list[j], _list[j+1] = _list[j+1], _list[j]
            flag = True
        counter+=1
        plt.bar(list(range(length)), _list)
        plt.pause(0.005)
        plt.clf()
    if not flag:
        break
plt.show()
print(_list)
print(counter)
