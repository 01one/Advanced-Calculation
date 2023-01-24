cpdef calculate(int x):
	cdef int i,j,y,a,b,k
	cdef list prime=[]
	for i in range(2,x+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			prime.append(i)
	y=len(prime)
	cdef list l=[]
	for i in range(y):
		for j in range(i+1):
			a=prime[i]
			b=prime[j]
			k=a+b
			if k==x:
				l.append([a,b])
	return l

cpdef result(int x):
	cdef i
	cdef list data=[]
	for i in range(4,x+1):
		if i%2==0:
			data.append([i,calculate(i)])
	return data
	
#python code	
"""	
#  Copyright 2021-2023 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
#Goldbach’s conjecture
#Any even number greater than 2 can be written as a sum of two primes.

x=eval(input("Enter an even number grater than two: "))
if x%2==0:
	prime=[]
	for i in range(2,x+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			prime.append(i)
	y=len(prime)

	l=[]
	for i in range(y):
		for j in range(i+1):
			a=prime[i]
			b=prime[j]
			k=a+b
			if k==x:
				l.append([a,b])
	print(l)
else:
	print("Enter an even number grater than two")
	
"""
