import copy
array = [[1, 5, 3], [2, 4, 12], [5, 6, 2]]
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



def forward_motion(a):
	i = 0
	j = 0
	m = 0
	for j in range(n):
		i = j
		for k in range(j+1, n):
			m = a[k][j] / a[i][j]
			a[k][j] = a[k][j] - m * a[i][j]
			for c in range(k, n):
				a[k][c] = a[k][c] - m * a[k-1][c]


	return a

print(forward_motion(array))








