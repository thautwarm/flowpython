#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: thautwarm

date: 25/07/17
"""

# =====================
# user configure files
pythonDistPath = './Python-3.6.2'  
flowpyDistPath = './PythonDist'
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
from utils import createTemp, isFileExists , fload, fsave, tryAction, joinPath
fdump = fsave

def fileGen(module, *presentnames: ["pythonDistPath","flowpyDistPath","tempfilesPath"] ):
    if len(presentnames)!=3: return BaseException("Params InputNum Do Not Match 3.")
    
    toRep, rep, temp = map(joinPath , presentnames ,(module, )*3 )
    
    for _ in map(isFileExists, (toRep, rep) ):pass

    createTemp(temp)

    _ = fload(toRep)
    fsave(_, temp)
    _ = fload(rep)
    fdump(_, toRep) 

    return "OK" 

for module in modules:
    fileGen(modules[module], pythonDistPath, flowpyDistPath, tempfilesPath )







