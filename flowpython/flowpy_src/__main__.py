import sys, os, platform, subprocess
from .flowpy_switcher.setupfile import setup 

getargs = .argv -> dict(tuples) where:
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

if __name__ == '__main__':
	dict_args     = getargs(sys.argv[1:])
	Arch          =  platform.architecture()[0]
	__Platform__  =  platform.platform().lower()

	if 'h' in dict_args:
		print("enable : python -m flowpy -m enable [-p PATH] \disable : python -m flowpy -m disable [-p PATH]")
		print("PATH : path of python intepreter.")
	else:
		assert 'm' in dict_args, "mode not selected: use command ' -m [enable|disable] ' "
		condic +[==] (dict_args["m"], Arch, __Platform__):
			case (mode, arch, platf) -> ('windows' in platf or 'linux' in platf) : True =>
				platf = 'windows' if 'windows' in platf else 'linux'
				pypath  = dict_args['p'] if 'p' in dict_args else getpypath() where:
					getpypath  = .-> ret where:
						try:
							ret = subprocess.Popen([search_command,'python'],stdout = subprocess.PIPE)\
								  .stdout\
								  .readlines()[0]\
								  .decode('utf8') where:
								search_command = 'where' if platf == 'windows' else 'which'
						except IndexError as e:
							raise BaseException('No python distribution found in PATH.') from e
				pypath -> setup(_, arch, platf)(mode)
			otherwise     => 
				raise BaseException('unknown platform...')



			




