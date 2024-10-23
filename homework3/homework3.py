from datetime import datetime

def funky_monkey():
	sysdate=datetime.today()
	print("Введите ваш день рождения в формате день,месяц,год")
	print("Введите exit для выхода")	
	try:
		ds=input()
		if ds=="exit" or ds=="Exit" or ds=="EXIT":
			exit()
		d,m,y=ds.split(",")
	except ValueError:
		print("Не по формату введена дата")
		return 1
	if (d.isdigit() and m.isdigit() and  y.isdigit())==False:
		print("Неверно введена дата")                 
		return 1
	d,m,y=int(d),int(m),int(y) 
	if d>31:
		print("Неверно введен день")                 
		return 1
	if (d<0 or y<0 or m<0)==True:
		print("Неверно введена дата")                 
		return 1
	dbdate=datetime(y,m,d)
	godik=sysdate.year-dbdate.year
	if (sysdate.month>=dbdate.month and  sysdate.day>dbdate.day and( sysdate.year-dbdate.year!=0)):
		godik=godik-1
	if godik<0:
		print("дата рождения меньше системной")
		return 1

	print(godik)
	return 0

while True:
	funky_monkey() 
		
	
		
