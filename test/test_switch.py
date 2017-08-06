

switch 1+2:
	case 1:
		print(False,1)
	case 2:
		print(False,2)
	case 3:
		print('switch test:pass 1')

switch "123":
	case "":
		print(False,3)
	case "abc":
		print(False,4)
	otherwise:
		print('switch test:pass 2')

a = [1,2,3,4,5]
b = list(range(1,6))
switch a:
	case [1,2,3] : 
		a+=a
		a+=a
		b =[1,2,3]
		print(False,a,b)
	case b:

		# test closure.
		b = 1
		assert(b == 1)
		b = 2
		assert(b == 2)
		b = 3
		assert(b == 3)
		print("switch test:pass 3")

assert(b == 3)



