#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: thautwarm

date: 25/07/17
"""
import time
# =====================
# user configure files
pythonDistPath = './PythonDist/{py_version}'
flowpyDistPath = './flowpython/{py_version}'  
tempfilesPath  = './temp_version/{py_version}/{commit_version}'
# ======================

support_version  =  ['py36','py35']
# =====================
# version info
__version__ = "0.2.2"
modules={
    'ast':'Python/ast.c',
    'symtable':'Python/symtable.c',
    'parser':'Parser/Python.asdl',
    'grammar':'Grammar/Grammar',
    'compile':'Python/compile.c',
    # 'acceler':'Parser/acceler.c'
}
# =====================

make_args={
    'clean':'make clean',
    'reconf': './configure CC=clang CXX=clang++ --without-gcc --with-pydebug',
    'clear':'make distclean',
    'grammar':'make regen-grammar',
    'ast':'make regen-ast',
    'all':['clear','reconf','grammar','ast'],
    'rev':['grammar','ast']
}


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
    
    version_now = fload(from_)
    fdump(version_now, _to)

    if temp:
        fsave(version_now, temp)

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
            read_in_arg_status = False

    if 'pyv' not in dict_args:
        dict_args['pyv'] = "py36"
    else:
        if dict_args['pyv'] not in support_version:
            raise Exception(f"Do not support version {dict_args['pyv']} \n Supported versions are {support_version}")
        
    dict_args['py_version'] = dict_args['pyv']
    action_version = dict_args['v'] if'v' in dict_args else time.time()
    tempfilesPath  = tempfilesPath.format(commit_version = action_version, py_version = dict_args['pyv'])
    pythonDistPath = pythonDistPath.format(py_version = dict_args['pyv']) 
    flowpyDistPath = flowpyDistPath.format(py_version = dict_args['pyv']) 
    
    def version_control(id_str):
        _to, from_ ,temp = (pythonDistPath, flowpyDistPath, tempfilesPath) if id_str == 'commit' else\
                           (flowpyDistPath, pythonDistPath, tempfilesPath) if id_str == 'back' else\
                           (pythonDistPath, tempfilesPath,  flowpyDistPath)
        for module in modules:
            fileGen(modules[module], _to, from_, temp )

    if   main_arg == 'commit':
        version_control('commit')
    elif main_arg == 'recover':
        version_control('recover')
    elif main_arg == 'back':
        version_control('back')
    elif main_arg == 'make':
        os.chdir(pythonDistPath)
        if 'm' not in dict_args:
            os.system("make")
        else:
            m = dict_args['m']
            if m in ['all','rev']:
                args = make_args[m]
                for arg in args:
                    os.system(make_args[arg])
                os.system("make")
            elif m in make_args:
                os.system(make_args[m])
    elif main_arg == 'test':

        os.chdir(pythonDistPath)
        testfilePath = '../test'

        if 'f' in dict_args:
            files = filter(lambda x:x, dict_args['f'].split(" "))
        else:
            files = os.listdir(testfilePath)
        files =map(lambda x: joinPath(testfilePath, x), files)
        for file in files:
            print('testing on {}'.format(file))
            os.system("./python {}".format(file))
    elif main_arg == 'run':
        os.system(f"{pythonDistPath}/python")
    else:
        print(BaseException("main argument cannot be identified."))
        pass


        








