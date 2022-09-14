""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. """
n = int(input('Введите число: '))

def get_fibonacci(n):
    list1 = []
    a, b = 1, 1
    for i in range(n):
        list1.append(a)
        a, b = b, a + b
    return list1

list_fib=get_fibonacci(n)
list2=list_fib.copy()
list_revers = []
for i in list2:
    list_revers.append(i*-1)
list_fib2=list_revers[::-1]
print(f'{list_fib2} 0 {list_fib}')