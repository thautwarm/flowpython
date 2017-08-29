# -*- coding: utf-8 -*-
def auto_logger(closure):
   if not isinstance(closure, dict):
       raise Exception("You should input a dict!!")
   globals().update(closure)
from collections import deque
class auto_compose:
    __slots__ = "compfunc"
    def __init__(self, func):
        self.compfunc = func if isinstance(func, deque) else deque([func])
    def __call__(self, *args, **kwargs):
        for func in self.compfunc:
            try:
                r = func(r)
            except:
                r = func(*args, **kwargs)
        return r
    def __getattribute__(self, name):
        if name.startswith("__") or name == 'compfunc':
            return super(auto_compose, self).__getattribute__(name)
        try:
            nextf =  globals()[name]
        except KeyError:
            if hasattr(__builtin__, name):
                nextf = getattr(__builtin__, name)
            else:
                raise Exception("Cannot find object {}".format(name))
        return auto_compose(deque([nextf])+self.compfunc)
    def __getitem__(self, v):
        maybe_curry = self(v)
        if callable(maybe_curry):
            return auto_compose(maybe_curry)
        return maybe_curry
from .fp import flat_map, flow_map, flow_reduce, flow_filter, foreach, groupby, fastmap, flatten, foldr, foldl

flat_map = auto_compose(flat_map)
flow_map = auto_compose(flow_map)
flow_filter = auto_compose(flow_filter)
foreach     = auto_compose(foreach)
groupby     = auto_compose(groupby)
fastmap     = auto_compose(fastmap)
flatten     = auto_compose(flatten)
foldr       = auto_compose(foldr)
foldl       = auto_compose(foldl)


