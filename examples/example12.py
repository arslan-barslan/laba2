print("Пример функции генератора")
def exmp(start=0, stop=5, step=1):
	chislo= start
	while chislo <=stop:
		yield chislo
		chislo +=start
rang=exmp(1,4)
for val in rang:
	print(val)
