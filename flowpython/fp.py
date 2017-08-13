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

# ===============

foreach = . self -> . f   -> None where:
        for item in self:
            f(item)

groupby = . self ->. function -> that where:
    that = defaultdict(list) 
    self -> foreach(_)(do) where:
        def do(item):
            that[function(item)].append(item) 


# map and reduce
# ====================
flow_map    = as-with *args def as f def map(f, *args)
flow_reduce = as-with *args def as f def reduce(f, *args)
## ===================
fastmap     = as-with *args def as f def (f(*items) for items in zip(*args))
fastmap.__doc__ = """Generators work faster! But they cannot be deepcopied in Python and can be evaluated only once. """
# ====================

flatten  = as-with seq:list def that where:
    def _f(seq:list):
        for item in seq:
            if not isinstance(item, list):
                yield item
            else:
                for item in _f(item): yield item
    that = _f(seq)

flat_map = flatten -> andThen(_)(flow_map)


# ==========================
# fold
foldr = . f -> . zero -> .seq -> ret where:
    warnings.warn("Not recommend to use 'fold' because there is no TCO in Python!")
    condic seq:
        case []     => ret = zero 
        +[]
        case (a,*b) => ret = f(a, foldr(f)(zero)(b))

foldl = . f -> . zero -> .seq -> ret where:
    warnings.warn("Not recommend to use 'fold' because there is no TCO in Python!")
    condic seq:
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
    fastmap = as-with *args def as f def [f(*items) for items in zip(*args)]
    flat_map = flatten -> andThen(_)(flow_map)


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

    







