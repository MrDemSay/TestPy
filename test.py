import copy
# a = [2, 3, 4]
# b = [4, 5, 6]
# e = [i * 2 for i in a]
#
# # for i in range(3):
# #     r = a[i] + b[i]
# #     e.append(r)
#
# print(e)
a = [[1, 2, 3], [5, 6, 7], [45, 7, 2]]
b = copy.deepcopy(a)
for i in range(len(b)):
    for j in range(len(b)):
        b[i][j] = b[i][j] * 2
print(b)
print(a)