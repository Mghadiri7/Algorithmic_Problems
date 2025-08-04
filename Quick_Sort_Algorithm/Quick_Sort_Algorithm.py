from random import randint as rnd
import matplotlib.pyplot as plt


def quick_sort(_list, low, high):
    if low<high:
        pivot = low
        i = low
        j = high
        while i<j:
            while _list[i]<=_list[pivot] and i<high:
                i+=1
            while _list[j]>_list[pivot]:
                j-=1
            if i<j:
                _list[i], _list[j] = _list[j], _list[i]

        _list[j], _list[pivot] = _list[pivot], _list[j]
        plt.bar(range(len(_list)), _list)
        plt.pause(0.005)
        plt.clf()

        quick_sort(_list, low, j-1)
        quick_sort(_list, j+1, high)
    return _list

length = 20
_list = [rnd(0, length) for i in range(50)]
print(_list)
print(quick_sort(_list, 0, len(_list)-1))
plt.bar(range(len(_list)), _list)
plt.show()