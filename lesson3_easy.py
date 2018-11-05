# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
import random

number = str(random.uniform(0.1, 100.1))
print(number)
ndigits = int(input("Сколько знаков после запятой оставить?"))

def my_round(number, ndigits):
	dotPos = number.find(".") #ищем точку в числе, чтобы дальше работать только с float
	numberAfterDot = number[dotPos+1::] #все числа после точки
	numberBeforeDot = number[:dotPos] #все числа до точки
	if ndigits > len(numberAfterDot):
		print("Ошибка, вы ввели слишком большое число")
	elif ndigits == 0:
		finalnumber = number[:dotPos+1]
		if int(number[dotPos+1]) >= 5:
			finalnumber = int(numberBeforeDot[:-1]) + 1
			return finalnumber
		elif int(number[dotPos+1]) <= 4:
			finalnumber = (numberBeforeDot[:-1])
			return finalnumber
	elif ndigits == len(numberAfterDot):
		print(number)
	elif ndigits > 0:
		if int(numberAfterDot[ndigits]) <= 4:
			finalnumber =  numberBeforeDot + "." + numberAfterDot[:ndigits]
			return finalnumber
		elif int(numberAfterDot[ndigits]) >= 5:
			finalnumber = numberBeforeDot + "." + numberAfterDot[:ndigits]
			lastNum = int(finalnumber[-1])
			if lastNum == 9:
				lastNum == 0
				lastNumber = int(finalnumber[-2])
				finalnumber =  numberBeforeDot + "." + numberAfterDot[:ndigits-2] + str(lastNumber+1) + str(lastNum)
			else:
				finalnumber = finalnumber[:-1] + str(lastNum+1)
				return finalnumber

print(my_round(number, ndigits))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
	sum_1 = ticket_number[0] + ticket_number [1] + ticket_number[2]
	sum_2 = ticket_number [3] + ticket_number[4] + ticket_number[5]
	if sum_2 == sum_1:
		print(bool(True))
	else:
		print(bool(0.0))

ticket_number = []
while len(ticket_number) <= 5:
	i = random.randint(0,9)
	ticket_number.append(i)
	i += 1

lucky_ticket(ticket_number)