#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
def Main():
    a = int(input('Введите первое число: '))
    i = int(input('Введите шаг: '))
    l = int(input('Введите предел: '))
    print(Rez(a, i, l))
def Rez(a, i, l):
    arr = []
    
    arr.append(a)
    j=1
    while(j<l):
        a=a+i
        arr.append(a)
        j+=1 
    return arr

Main()