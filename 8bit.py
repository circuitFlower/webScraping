import random
list = [0,0,0,0,0,0,0,0]
x = len(list)
y=0
for c in range(0,10):
	for i in range(x):
		list[i]=c
		print list
		list[i]=0
