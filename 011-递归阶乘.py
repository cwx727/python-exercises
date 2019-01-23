#including utf-8

def factorial(n):
	res = n
	if n>1:
		res = res*factorial(n-1)
	else:
		res =1
	return res

result = factorial(10)
print(result)
		
