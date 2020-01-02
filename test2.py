I = input().split(',')
A = ''

for i in I:
	if len(i) < 6 or len(i) > 12:
		continue
	f = [0,0,0,0]
	for j in i:
		if ord(j) >= 65 and ord(j) <= 90:
			f[1] = 1
		if ord(j) >= 97 and ord(j) <= 122:
			f[0] = 1
		if ord(j) >= 48 and ord(j) <= 57:
			f[2] = 1
		if j == '$' or j == '#' or j == '@':
			f[3] = 1
	if not 0 in f:
		A = A + i + ','
A = A[:-1]
print(A)