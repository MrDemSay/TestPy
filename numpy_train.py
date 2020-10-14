array = [[0, 2, 3], [0, 6, 7], [45, 7, 2]]

# чтобы в первой строке небыло элемента = 0 (WORKING)


def scan_on_zero(a):
	for i in range(len(array)):
		i = 0
		for j in range(len(array[i])):
			if array[i][0] == 0:
				q = array[i]
				array.remove(q)
				array.append(q)
			else:
				break
		break


scan_on_zero(array)




# for i in range(3):
# 	for j in range(3):
# 		if array[i][0] == 0:
#
#



	#print(array[i])
#
# a = 0
# while a < 3:
# 	i, j = a, a
# 	a += 1
#
# 	e = []
# 	for i in range(3):
# 		e.clear()
# 		c = array[i+1]
# 		q = -(array[i + 1][j] / array[i][j])
# 		for j in range(3):
# 			w = array[i][j] * q
# 			e.append(w)
#
# 		r = []
# 		for y in range(3):
# 			r.append(c[y] + e[y])
# 		array.remove(array[i+1])
# 		array.insert(i+1, r)
#
# 	print(e)
# 	print(array)



