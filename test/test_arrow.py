assert 1 -> 2 == 2
print("pass: 1->2 == 2 ")
assert 1 -> _ == 1
print("pass: 1 -> _ == 1")
assert [1,2,3] -> map(.x->x+1, _) -> list(_) -> print(_) or True
print('pass: ...')
assert range(100) -> reduce(.x,y->x+y, _) -> print(_)  or True where:
    from functools import reduce
print('pass: ...')


foreach = .self, f -> None where:
        for item in self:
            f(item)

groupby = .self, f -> ret where:
        ret = defaultdict(list) where:
                from collections import defaultdict
        self -> foreach(_, setv) where:
                setv = .item -> None where:
                    ret[f(item)].append(item)
        
range(20) -> groupby(_, .x->x%2) -> print(_)

