# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint

print('Введите длину массива N:')
n= int(input())

arr=[]
for i in range(n):
    arr.append(randint(1, 10))  
print(arr)

print('Введите число Х:')
x = int(input())

res = arr[0]
for i in arr:
    if abs(i - x) < abs(res - x):
        res = i

print(res)
