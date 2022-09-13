"""     Напишите программу, которая найдёт произведение пар чисел списка.
    Парой считаем первый и последний элемент, второй и предпоследний и т.д. """

from random import randint


lst = [randint(1,5) for i in range(5)]
print(lst)
second_lst = []
for i in range (len(lst)+1//2):
    second_lst.append(lst[i]*lst[len(lst)-1-i])
print(second_lst)