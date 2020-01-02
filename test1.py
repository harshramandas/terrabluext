def check(binary):  
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    if decimal % 5 == 0:
    	return True
    else:
    	return False
    	
I = input().split(',')
A = ''
for i in I:
	n = int(i)
	if check(n):
		A = A+i+','
A = A[:-1]
print(A)