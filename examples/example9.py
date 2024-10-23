print("Пример внутренней функции")
def outer(out_par1):
	def inner(in_par1):
		return f'значение внешней переменной: {in_par1}'
	return inner(out_par1)
print(outer('Test'))
