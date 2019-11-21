# Muallif: Otaboboyev Akmal 
# https://t.me:@akmal1st
# ildiz chiqarish dasturi v2.0
from math import ceil

def ildiz2(a):
	x = ceil(len(str(int(a)))/2)
	a = a/(100**(x-1))
	c = []
	b = 0
	for k in range(52):
		for i in range(9,-1,-1):
			j = (b*2*(10**k)+i)*i
			if j<=a:
				a=(a-j)*100
				
				if k==1:
					c.append(".")
				
				c.append(i)
				b = ltof(c)
				break
	d = b - int(b)
	if d==0:
		f = [b]
		return f
	else:
		ns(c,x)
		return c
def ltof(lst):
	s = ''
	for i in range(len(lst)):
		s=s+str(lst[i])
	ss = float(s)
	return ss
def ns(c,x):
	if '.' in c:
		for i in range(1,x):
			b = c[i]
			c[i] = c[i+1]
			c[i+1] = b

print("#"*30)
a = float(input("Son kiriting: "))
print("#"*30)
k = ildiz2(a)
for i in k:
	print(i,end='')
print()