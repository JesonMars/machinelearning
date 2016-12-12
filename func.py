from numpy import *

def fun1(i):
	return i%4+2

def fun2(i,j):
	return (i+1)*(j+1)

print fromfunction(fun1,(10,))
print fromfunction(fun2,(9,9))

