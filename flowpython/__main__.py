# -*- coding: utf-8 -*-

import sys, os, platform, subprocess
from .flowpy_switcher.setupfile import setup 

def getargs(argv):
	tuples = []
	def gen(key):
		if key.startswith("-"):
			key = key[1:]
			if key == 'h':
				tuples.append((key,'True'))
				return gen
			def setarg(value):
				tuples.append( (key,value) )
				return gen
			return setarg				
		else:
			return gen
	op = gen
	for arg in argv:
		op = op(arg)
	return dict(tuples)
	
if __name__ == '__main__':
	dict_args     = getargs(sys.argv[1:])
	Arch          =  platform.architecture()[0]
	__Platform__  =  platform.platform().lower()

	if 'h' in dict_args:

		print("enable : python -m flowpy -m enable [-p PATH] \disable : python -m flowpy -m disable [-p PATH]")
		print("PATH : path of python intepreter.")
	
	else:
		
		assert 'm' in dict_args, "mode not selected: use command ' -m [enable|disable] ' "
		
		pattern_match_test = (dict_args["m"], Arch, __Platform__)
		
		try:
			(mode, arch, platf) = pattern_match_test
			jd = 'windows' in platf or 'linux' in platf
			if not jd: 
				raise EnvironmentError("unsupported os")
			platf = 'windows' if 'windows' in platf else 'linux'
			def getpypath():
				try:
					search_command = 'where' if platf == 'windows' else 'which'
					ret = subprocess.Popen([search_command, 'python'],stdout = subprocess.PIPE)\
							.stdout\
							.readlines()[0]\
							.decode('utf8') 
				except IndexError as e:
					raise BaseException('No python distribution found in PATH.') from e
				return ret
			pypath  = dict_args['p'] if 'p' in dict_args else getpypath()
			setup(pypath, arch, platf)(mode)

		except Exception as e:
			
			raise BaseException('unknown platform...') from e





			




