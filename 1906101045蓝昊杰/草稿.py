l=[1]
for i in range(6,10000):
	for j in range(2,int(i**0.5)+1):
		if i%j==0:
			l.append(j)
			l.append(i/j)
	s=sum(l)
	l=[1]
	if s==i:
		print(i)