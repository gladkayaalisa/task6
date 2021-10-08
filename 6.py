try:
	print("Какое количество элементов должно быть в массиве?")
	a = int(input())
	array = [0] * a
	for i in range (len(array)):
		i = str(i + 1)
		print ("Введите элемент " + i, end = ": ")
		i = int(i)
		i = i -1
		array[i] = int(input())
	print ("Введите DELTA:")
	delta = int(input())
	least = array[0] if array else None
	for i in array:
		if i < least:
			least = i
	x = delta + least
	l = 0
	for i in array:
		if i == x:
			l+=1
		print ("Результат: ", l)
except ValueError:
	print("Incorrect_data")