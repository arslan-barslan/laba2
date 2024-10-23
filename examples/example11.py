print("Пример лямбды функции которая выводит список прочитанных книг")
def exmp(books,func):
	for book in books:
		print(func(book))
books = ['System Design','Python и DevOps','Git. Практическое руководство']


exmp(books, lambda book: book.upper() + ' - прочитано')
