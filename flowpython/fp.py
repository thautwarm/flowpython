#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 12:48:26 2017

@author: thautwarm
"""
from collections import defaultdict
from functools import reduce
import warnings
# ===============
# Basic

compose = .f1 -> .f2 -> . *args, **kwargs -> f2(*args, **kwargs) -> f1(_)
andThen = .f1 -> .f2 -> . *args, **kwargs -> f1(*args, **kwargs) -> f2(_)

def AndThen(*func_stack):
    def _1(*args, **kwargs):
        for func in func_stack:
            try:
                mid = func(mid)
            except:
                mid = func(*args, **kwargs)
        return mid
    return _1

def Compose(*func_stack):
    def _1(*args, **kwargs):
        for func in func_stack[::-1]:
            try:
                mid = func(mid)
            except:
                mid = func(*args, **kwargs)
        return mid
    return _1
            


# ===============

foreach = . f       ->. self  -> None where:
        for item in self:
            f(item)

groupby = . function ->. self -> that where:
    that = defaultdict(list) 
    self ->> foreach(do) where:
        def do(item):
            that[function(item)].append(item) 


# map and reduce
# ====================
flow_map    = as-with f def as *args def map(f, *args)
flow_filter = as-with f def as *args def filter(f, *args)
flow_reduce = as-with f def as *args def reduce(f, *args)
## ===================
fastmap     = as-with f def as *args def (f(*items) for items in zip(*args))
fastmap.__doc__ = """Generators might work faster! Howerver they cannot be deepcopied in Python and can be evaluated only once. """
# ====================

flatten  = as-with seq:list def that where:
    def _f(seq:list):
        for item in seq:
            if not isinstance(item, list):
                yield item
            else:
                yield from _f(item)
    that = _f(seq)

flat_map = lambda f: andThen(flatten)(flow_map(f))


# ==========================
# fold
foldr = . f -> . zero -> .seq -> ret where:
    warnings.warn("Not recommend to use 'fold' because there is no TCO in Python!")
    condef seq:
        case []     => ret = zero 
        +[]
        case (a,*b) => ret = f(a, foldr(f)(zero)(b))

foldl = . f -> . zero -> .seq -> ret where:
    warnings.warn("Not recommend to use 'fold' because there is no TCO in Python!")
    condef seq:
        case []     => ret = zero
        +[]
        case (*a,b) => ret = f(foldl(f)(zero)(a), b)
        
# ===========================

class strict:
    """
    Some method implemented with recursion.
    """
    flatten = as-with seq:list def that where:
        that = []
        def _f(seq:list):
            for item in seq:
                if not isinstance(item, list):
                    that.append(item)
                else:
                    _f(item)
        _f(seq)
    fastmap = as-with f def as *args def [f(*items) for items in zip(*args)]
    flat_map = lambda f: andThen(flatten)(flow_map(f))


class norecursion:
    """
    Some method implemented without recursion.
    In most case, these methods are not recommended as a result of the very slow "while" in Python.abs
    However, if the algorithm bears the risk of StackoverflowError, these methods deserve to be tried. 
    """
    class lazy:
        @staticmethod
        def flatten(seq:list):
            """
            this is the implementation of function flatten without recursion.
            """
            head  = [] 
            tmp   = seq
            idx   = [0]
            while True:
                try:
                    item = tmp[idx[-1]]
                except IndexError:
                    try:
                        tmp = head.pop()
                        idx.pop()
                        continue
                    except IndexError:
                        break
                idx[-1] += 1
                if not isinstance(item, list):
                    yield item 
                else:
                    head.append(tmp)
                    tmp = item
                    idx.append(0)
    
    class strict:
        @staticmethod
        def flatten(seq:list):
            """
            this is the implementation of function flatten without recursion.
            """
            head  = [] 
            store = []
            tmp   = seq
            idx   = [0]
            while True:
                try:
                    item = tmp[idx[-1]]
                except IndexError:
                    try:
                        tmp = head.pop()
                        idx.pop()
                        continue
                    except IndexError:
                        break
                idx[-1] += 1
                if not isinstance(item, list):
                    store.append(item) 
                else:
                    head.append(tmp)
                    tmp = item
                    idx.append(0)
            return store

    







