array = [[1, 5, 3], [2, 4, 12], [5, 6, 2]]
b = [1, 3, 5]
n = 3


def scan_on_zero(a):
	# чтобы в первой строке небыло элемента = 0 (WORKING)
	for i in range(len(a)):
		i = 0
		for j in range(len(a[i])):
			if a[i][0] == 0:
				q = a[i]  # сохраняем в переменную
				a.remove(q)  # удаляем целую строку (содержимое строки сохраняется)
				a.append(q)  # вставляем удалённую строку в конец
			else:
				break
		break


scan_on_zero(array)


def forward_motion(a, b):
	x = []

	for k in range(0, n):
		x.append(0)
		for j in range(k+1, n):
			d = a[j][k] / a[k][k]
			for i in range(k, n):
				a[j][i] = a[j][i] - d * a[k][i]
			b[j] = b[j] - d * b[k]

	for k in range(n-1, 0, -1):
		d = 0
		s = 0
		for j in range(k, n):
			s = a[k][j] * x[j]
			d = d + s
			x[k] = (b[k] - d) / a[k][k]
	print('Result: ')

	for i in range(0, n):
		print('x [', i, '] = ', x[i])


forward_motion(array, b)








