#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:36:58 2017

@author: thautwarm
"""

"""
this module is just for fun!!!
"""
from copy import deepcopy
permutations = .seq -> seq_seq where:
    condic+[] seq:        
        case (a,  ) => seq_seq = [a,]        
        case (a, b) => seq_seq = [[a,b],[b,a]]        
        case (a,*b) => 
            seq_seq = permutations(b) -> map(.x -> insertAll(x, a),  _) -> sum(_, []) where:
                insertAll = . x, a -> ret where:
                    ret = [ deepcopy(x) -> _.insert(i, a) or _ for i in  (len(x) -> range(_+1))  ]
                        
                