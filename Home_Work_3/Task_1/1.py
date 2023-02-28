# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

print('Введите длину массива N:')
n= int(input())

arr=[]
for i in range(n):
    arr.append(randint(1, 10))  
print(arr)
print('веедите число Х:')
x = int(input())
count = 0
for i in range(n):
    if x == arr[i]:
        count +=1
print(count)        
