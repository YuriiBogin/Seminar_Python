# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
#если получается некорректное разделение - напечатать "Неверное S"

print('Введите число S:')
s = int(input())
katy = int((s/3)*2)
pety = int((katy/2)/2)
ser = int(pety)
if (pety+ser)*2 == katy:
    print(pety, katy, ser)
else:
    print('Введите другое число S')