from random import *

def generate_rps():
	x=randint(0,2)
	return x


def interp(x):
	if x=="Камень":
		return 0
	if x=="Ножницы":
		return 1
	if x=="Бумага":
		return 2

def win_interp(w,q):
	lis=['Камень','Ножницы','Бумага']
	print("робот: ",lis[q])
	if w==1:
		print("Вы выиграли!")
	elif w==2:
		print("Вы проиграли!")
	else:
		print("Ничья!")		



def maingameplay(skip):
	if skip==False: 
		print("Игра в камень ножницы бумага!")
		print("Правила Игры")
		print("Победитель определяется по следующим правилам:     Камень побеждает ножницы («камень затупляет или ломает ножницы»)     Ножницы побеждают бумагу («ножницы разрезают бумагу»)     Бумага побеждает камень («бумага заворачивает камень»)")
	print("Введите ваш знак в формате 'Камень','Ножницы' или 'Бумага'")
	try:
		user=input()
		if not(user=="Камень" or user=="Ножницы" or user=="Бумага")==True:
			print("Ошибка! Неверный ввод Введите в формате 'Камень','Ножницы' или 'Бумага' ")
			return maingameplay(True) 			
		x=interp(user)
		bot= generate_rps()
		win=0
		if x==0 and bot == 1:
			win=1
		if x==0 and bot == 2:
			win=0 
		if x==bot:
			win=3
		if x==1 and bot == 0 :                        
			win=0
		if x==1 and bot == 2:                         
			win=1  
		if x==bot:                         
			win=3
		if x==2 and bot == 0:                        
			win=1  
		if x==2 and bot == 1:                      
			win=0
		if x==bot:                         
			win=3
		win_interp(win,bot)
	except ValueError:
		print("Неверный ввод")
		return maingameplay(True)		

maingameplay(False)
