""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на нечётной позиции. """
from random import randint


lst = [randint(-5,15) for i in range(8)]
print(lst)
print (sum(lst[1::2]))