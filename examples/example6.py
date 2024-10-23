print("Пример функции c позиционными аргументами")
def exmp(name,color,age):
	return {'name': name, 'color': color, 'age': age}
cat=exmp(color='Черно-белый',age=1,name='Груша')
print(cat)
