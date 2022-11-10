def isNumber(strNumber, isFloat = False):
	if isFloat:
		hourlyRateIsFloat = "." in strNumber
		if hourlyRateIsFloat:
			partitions = strNumber.split('.')
			if partitions[0].isdigit() and partitions[0].isdigit():
				return True
			else:
				return False
		else:
			if strNumber.isdigit():
				return True
			else:
				return False
	else:
		numbers = '0123456789'
		for strNum in strNumber:
			if strNum not in numbers:
				return False
		return True


def getEmployees():
	employees = input('Укажите количество сотрудников: ')
	if isNumber(employees):
		return int(employees)
	else:
		print('Ошибка, введите целое число!\n')
		getEmployees()
		
	
def gethourlyRate():
	hourlyRate = input('Введите почасовую ставку оплаты: ')
	if isNumber(hourlyRate, True):
		return float(hourlyRate)
	else:
		print('Ошибка, введите число!\n')
		gethourlyRate()


def getHours(employess):
	hours = []
	i = 1
	while i <= employess:
		hour = input(f'Введите число отработанных часов сотрудником {i}: ')
		if isNumber(hour):
			hours.append(float(hour))
			i += 1
		else:
			print('Ошибка: введите число!\n')
			continue
			
	return hours
		

def printGrossPay(employees, hours, hourlyRate):
	i = 0
	while i < employees:
		grosspay = hours[i] * hourlyRate
		print(f"Зарплата сотрудника {i + 1}: {grosspay} р.")
		i += 1


def main():
	employees = getEmployees()
	hourlyRate = gethourlyRate()
	hours = getHours(employees)
	printGrossPay(employees, hours, hourlyRate)
	
			
main()
