print("Пример внутренней функции")
def outer(out_par1):
	def inner2():
		return f'значение внешней переменной: {out_par1}'
	return inner2
x=outer('Test')
print(x())
