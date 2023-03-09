# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую неотрицательную степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def power(base, step):
    if (step == 1):
        return (base)
    if (step != 1):
        return (base * power(base, step - 1))
base = int(input("Введите число: "))
step = int(input("Введите степень числа: "))
print("Результат возведения в степень равен:", power(base, step))