print('test_where')
1 where:
	a = 1
print(a == 1)

# ============================================
a = ret where:
	ret = 10
print(a == 10)


# ============================================
a = ret1*ret2 where:
	ret1 = ret2*r where:
		r	 = 10
		ret2 = 2
print(a == 40)

# ============================================
from math import pi
r = 1  # the radius
h = 10 # the height

S = (2*S_top + S_side) where:
    S_top  = pi*r**2
    S_side = C * h where:
        C = 2*pi*r
	

