assert 1 -> 2 == 2
print("pass: 1->2 == 2 ")
assert 1 -> _ == 1
print("pass: 1 -> _ == 1")
assert [1,2,3] -> map(.x->x+1, _) -> list(_) -> print(_) or True
print('pass: ...')
assert range(100) -> reduce(.x,y->x+y, _) -> print(_)  or True where:
    from functools import reduce
print('pass: ...')


