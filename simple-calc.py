def plus(a, b):
	return print(a + b)

def minus(a, b):
	return print(a - b)

def multi(a, b):
	return print(a * b)

def split(a, b):
	return print(a / b)

def main():
	print('ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР!')

	while True:
		operation = str(input('Введите знак операции или q чтобы закончить: '))

		if (operation == 'q'):
			print('ПОКА!')
			break
	
		num1 = int(input('Первое число: '))
		num2 = int(input('Второе число: '))

		if(operation == '+'):
			plus(num1, num2)

		if(operation == '-'):
			minus(num1, num2)
	
		if(operation == '/'):
			split(num1, num2)

		if(operation == '*'):
			multi(num1, num2)


main()