#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: thautwarm

date: 25/07/17
"""

# =====================
# user configure files
pythonDistPath = './Python'  
flowpyDistPath = './flowpy'
tempfilesPath  = './temp'
# ======================

# =====================
# version info
__version__ = 0.1
modules={
    'ast':'Python/ast.c',
    'symtable':'Python/symtable.c',
    'parser':'Parser/Python.asdl',
    'grammar':'Grammar/Grammar'
}
# =====================



import os
from utils import createTemp, isFileExists , fload, fsave 
fdump = fsave

def fileGen(module, *presentnames: ["pythonDistPath","flowpyDistPath","tempfilesPath"] ):
    if len(presentnames)!=3: return BaseException("Params InputNum Do Not Match 3.")
    
    toRep, rep, temp = map(os.path.join , presentnames ,(module)*3 )
    
    for _ in map(isFileExists, (toRep, rep) ):pass

    createTemp(temp)

    tryAction("fload(toRep)")
    tryAction("fsave(_, temp)")
    tryAction("fload(rep)")
    tryAction("fdump(_, toRep)") 

    return "OK" 

for module in modules:
    fileGen( module, pythonDistPath, flowpyDistPath, tempfilesPath )







