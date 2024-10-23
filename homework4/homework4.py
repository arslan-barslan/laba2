import random

def podschet(x):
	chisel=[random.randint(0, 200) for i in range(10)]
	mult=list(filter(lambda num: num % x == 0, chisel))
	if mult:
		return mult
	else:
		print("нет кратных чисел")
		return None
x=int(input("Введите число X: "))
y=podschet(x)
print("Сгенерированные числа:", y)

