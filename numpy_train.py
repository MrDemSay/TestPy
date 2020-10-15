import copy
array = [[1, 5, 3], [2, 9, 7], [15, 6, 2]]
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
	b = copy.deepcopy(a)

	q = 0
	m = 0
	i = 0
	while i < n:
		k = i
		for j in range(n):
			m = a[k+1][q] / a[q][q]
			b[k+1][j] = a[k+1][j] - m * a[q][j]


		i += 1

forward_motion(array)








