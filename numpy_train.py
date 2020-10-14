array = [ [0, 2, 3],
		  [5, 6, 7],
		  [45, 7, 2] ]

		#чтобы в первой строке небыло элемента = 0
		for i in range(3):
			for j in range(3):
				if array[0][0] == 0:
					q = array[0]
					array.remove(q)
					array.append(q)

			#print(array[i])


		i = 0
		j = 0
		for i in range(3):
			e = []
			c = array[i+1]
			q = -(array[i + 1][j] / array[i][j])
			for j in range(3):
				w = array[i][j] * q
				e.append(w)

			r = []
			for y in range(3):
				r.append(c[y] + e[y])
			array.remove(array[i+1])
			array.insert(i+1, r)

		print(e)
		print(array)



