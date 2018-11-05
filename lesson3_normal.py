# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

#def fibonacci(n, m):

def fib(n, m):
	f = [1, 1]
	for i in range(2, m+1):
		f.append(f[i-1] + f[i-2])
	print(f[n-1:m+1])

fib(5, 9)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass

import random 
n = int(input("Ввести кол-во элементов"))
origin_list = []
while len(origin_list) <= n-1:
	i = random.randint(0,100)
	origin_list.append(i)
	i += 1
print(origin_list)

def sort_to_max(origin_list):
	n = 1
	while n < len(origin_list):
		for i in range(len(origin_list)-n):
			if origin_list[i] > origin_list[i+1]:
				origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
		n += 1
	return origin_list

print(sort_to_max(origin_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_1(lists, restrict):
	result = []
	n = 1
	while n <= len(lists):
		for i in range(len(lists)):
			if lists[i] >= restrict:
				result.append(lists[i])
		n += 1
	print(set(result))
	return set(result)
	

filter_1([3, 21, 67, 89, 4, 5, 7, 8, 9], 6)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

