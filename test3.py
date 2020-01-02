import operator
n = int(input("Enter no. of rows/records: "))
A = []
for i in range(n):
	j = tuple(input().split(','))
	A.append(j)
A.sort(key = operator.itemgetter(0, 1, 2))
print(A)