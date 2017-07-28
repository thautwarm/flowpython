#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: thautwarm

date: 25/07/17
"""
import time
# =====================
# user configure files
pythonDistPath = './PythonDist'
flowpyDistPath = './flowpy'  
tempfilesPath  = './temp_version/{}'
# ======================

# =====================
# version info
__version__ = 0.1
modules={
    'ast':'Python/ast.c',
    'symtable':'Python/symtable.c',
    'parser':'Parser/Python.asdl',
    'grammar':'Grammar/Grammar',
    'compile':'Python/compile.c'
}
# =====================


import sys
import os
from utils import createTemp, isFileExists , fload, fsave, tryAction, joinPath
fdump = fsave


def fileGen(module, *presentnames: ["pythonDistPath","flowpyDistPath","tempfilesPath"] ):
    if len(presentnames)!=3: return BaseException("Params InputNum Do Not Match 3.")
    
    _to, from_, temp = map(joinPath , presentnames ,(module, )*3 )
    
    for _ in map(isFileExists, (_to, from_) ) : pass
    
    if temp:
        createTemp(temp)
    
    _ = fload(_to)

    if temp:
        fsave(_, temp)
    
    _ = fload(from_)
    fdump(_, _to) 

    return "OK" 


if __name__ == '__main__':
    argv = sys.argv[1:]

    # this is a initial version of project-manager which means it's quite incomplete.
    
    main_arg = argv[0]
    dict_args=dict()
    read_in_arg_status = False

    for arg_i in argv:
        if arg_i.startswith('-'):
            key = arg_i[1:]
            read_in_arg_status = True
        elif read_in_arg_status:
            dict_args[key] = arg_i

    
    action_version = dict_args['v'] if'v' in dict_args else time.time()
    tempfilesPath = tempfilesPath.format(action_version)

    def actions(id_str):
        _to, from_ ,temp = (pythonDistPath, flowpyDistPath, tempfilesPath) if id_str == 'commit' else\
                           (flowpyDistPath, pythonDistPath, tempfilesPath) if id_str == 'back' else\
                           (pythonDistPath, tempfilesPath,  flowpyDistPath)
        for module in modules:
            fileGen(modules[module], _to, from_, temp )

    if   main_arg == 'commit':
        actions('commit')
    elif main_arg == 'recover':
        actions('recover')
    elif main_arg == 'back':
        actions('back')
    else:
        print(BaseException("main argument cannot be identified."))
        pass


        








