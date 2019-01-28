import itertools
list = [0,0,0,0,0,0,0,0]
for L in range(0, 8):
	for subset in itertools.combinations(list, L):
		for x in range(0,8):
			list[x]=L
			print(subset)
