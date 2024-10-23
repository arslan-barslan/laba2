print("Пример внутренней функции")
def outer(out_par1, out_par2):
	def inner(in_par1,in_par2):
		return in_par1+in_par2
	return inner(out_par1, out_par2)
print(outer(5,6))
