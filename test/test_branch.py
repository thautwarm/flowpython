print("branches No.1:")
| 1==2 => a = False
| 2==3 => a = False
| 3    => a = True
print(f'branch res is {a}')

b = ret where:
    | 1 == 2 => ret = 1
    | 2 == 2 => ret = 2
assert b == 2

otherwise = True
x = 2

| x == 1           => x += 1
| type(x) is str   => x = int(x) 
| otherwise        =>
        x = 2*x
        y = 1
def defined(key):
    return key in globals()

assert x == 4
print('Is y defined? => ',defined("y"))