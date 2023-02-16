# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданногомаксимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint

n=int(input('Введите количесиво элементов '))
minim=int(input('Минимум '))
maxim=int(input('Максимум '))

my_list1=[]
my_list2=[]

for i in range(n):
    my_list1.append(randint(-10,10))

print(my_list1)

for i in range(n):
    if minim<=my_list1[i]<=maxim:
        my_list2.append(my_list1[i])

print(my_list2)
