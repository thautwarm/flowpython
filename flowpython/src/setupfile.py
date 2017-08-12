class windows:
	reps = {
		'python3.dll',
		'python36.dll',
		'pythonw.exe',
		'python.exe'
		}
class linux:
	reps = {
	'python'
		}

import os
from . import __file__ as rootpath
from .utils import makedir_from, moveto, bin_copyto
cat = os.path.join
def setup(path, arch, platform):
	flowpy_dir_path = cat(makedir_from(rootpath),f"{platform}-{arch}") 
	save_dir_path   = cat(makedir_from(rootpath),'origin_py') 
	origin_dir_path = makedir_from(path)
	reps = eval(f"{platform}.reps")
	def install():
		for rep in reps:
			oripy_file  = cat(origin_dir_path, rep)
			flowpy_file = cat(flowpy_dir_path, rep)
			save_file   = cat(save_dir_path  , rep)  # save the original python intepreter in case of uninstalling.
			oripy_file  -> moveto(_, save_file)
			flowpy_file -> bin_copyto(_, oripy_file)
			print(f"installed -- {rep}")
		if platform == 'linux':
			os.system(f'chmod 777 {path}')
	def uninstall():
		for rep in reps:
			oripy_file  = cat(origin_dir_path, rep)
			save_file   = cat(save_dir_path  , rep)
			save_file   -> moveto(_, oripy_file)
			print(f"uninstalled -- {rep}")
		if platform == 'linux':
			os.system(f'chmod 777 {path}')
	return .option -> ret() where:
		ret = install   if option == 'install'   else \
			  uninstall if option == 'uninstall' else \
			  .-> print(f'No option called {option} => do nothing.')	  
