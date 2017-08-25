
f = .x -> r where:
    condic x:
        [==]
        case []             =>  r = 0

        +[==]
        case (a,*b) -> b:[] =>  r = a

        otherwise           =>  r= a + f(b)

        

from flowpython.fp import flow_map, flat_map,flatten, andThen, fastmap, flow_reduce
a = [[1,2,3],[3,4,6], [2,3,4,5,6,7,8],[2,3,4,5,1,2,3]]
fast_flat_map = lambda f: andThen(flatten)(fastmap(f))
def test1():
    a ->> fast_flat_map(.x->x+1) => list
def test2():
    a ->> flat_map(.x->x+1) => list 
a ->> fast_flat_map(.x->x+1) => list => flow_reduce(.x,y->x-y) => print