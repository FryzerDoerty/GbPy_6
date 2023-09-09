#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
def Main():
    random_list = [randint(1, 100) for i in range(10)]
    print(random_list)
    min = int(input('Введите минимум в диапазоне от 1, до 100:'))
    max = int(input('Введите максимум в диапазоне от 1, до 100:'))
    print(Rez(min, max, random_list))
def Rez(min, max, random_list):
    i=0
    arr=[]
    while(i<len(random_list)):
        if(random_list[i]<max and random_list[i]>min):
            arr.append(i)
        i+=1
    return arr
Main()