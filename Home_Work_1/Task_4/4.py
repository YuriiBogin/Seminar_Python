# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
print('Введите размер шоколадки n x m')
print('n=', end=' ')
n = int(input())
print('m=', end=' ')
m = int(input())
print('Введите количество долек К =', end=' ')
k = int(input())

if k % n == 0 or k  % m == 0:
    print('YES')
else:
    print('NO')
