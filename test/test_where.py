1 where:
	with-in
		a=1
	with-break
print(a)

a = ret where:
	with-in
		ret = 10
	with-break
print(a)

a = ret1*ret2 where:
	with-in
		ret1 = ret2*r where:
			with-in
				r=10
				ret2=2
			with-break
	with-break

