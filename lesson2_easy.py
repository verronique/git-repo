#__author__ Veronika Zelenkevich
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for fruit in fruits:
	print(i, ".", '{:>10}'.format(fruit))
	i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = input("Введите любые элементы данного списка, разделяя элементы запятыми").split(",")
list_2 = input("Введите любые элементы данного списка, разделяя элементы запятыми").split(",")
list_1 = list(set(list_1).difference(set(list_2)))
print("Преобразованный первый список", list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_1 = list(input("Введите любые числовые элементы данного списка, разделяя элементы запятыми").split(","))
list_2 = []
for i in list_1:
	if int(i) % 2 == 0:
		list_2.append(int(i)/4)
	else:
		list_2.append(int(i)*2)
print(list_2)