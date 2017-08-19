# -*- coding: utf-8 -*-
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

import os,json
from flowpython import __file__ as rootpath
from .utils import makedir_from, moveto, bin_copyto
try:
	user_path = os.environ["HOME"]
except KeyError:
	user_path = os.environ["HOMEPATH"]

cat = os.path.join
def setup(path, arch, platform):
	flowpy_dir_path = cat(makedir_from(rootpath),f"{platform}-{arch}") 
	save_dir_path   = cat(makedir_from(rootpath),'origin_py') 
	origin_dir_path = makedir_from(path)
	reps            = eval(f"{platform}.reps")
	manager_path    = cat(user_path, '.flowpy')
	def enable():
		if not os.path.exists(manager_path):pass
		else:
			with open(manager_path, 'r') as f:
				condic f:
					+[==]
					case a -> json.load(a)['enabled']:'true'  =>
						print("Flowpython has been enabled.")
						reps.clear()
					otherwise =>
						pass
		if reps:
			for rep in reps:
				# ================== ENABLE
				oripy_file  = cat(origin_dir_path, rep)
				flowpy_file = cat(flowpy_dir_path, rep)
				save_file   = cat(save_dir_path  , rep)  # save the original python intepreter in case of uninstalling.
				oripy_file  -> moveto(_, save_file)
				flowpy_file -> bin_copyto(_, oripy_file)
				# ================== 
				f"enabled -- {rep}" -> print(_)
			if platform == 'linux':
				os.system(f'chmod 777 {path}')
			with open(manager_path, 'w') as f:
				{'enabled':'true'} -> json.dump(_, f)

	def disable():
		if not os.path.exists(manager_path): 
			print("Disable before enabled!!!")
			return
		with open(manager_path, 'r') as f:
			condic f:
				+[==]
				case a -> json.load(a)['enabled']:'true' =>
					for rep in reps:
						# ================== DISABLE
						oripy_file  =  cat(origin_dir_path, rep)
						save_file   =  cat(save_dir_path  , rep)
						save_file   -> moveto(_, oripy_file)
						f"disabled -- {rep}" -> print(_)
						# ==================
					if platform == 'linux':
						os.system(f'chmod 777 {path}')
					with open(manager_path, 'w') as f:
						{'enabled':'false'} -> json.dump(_, f)

				otherwise =>
					print("Flowpython hasn't been enabled yet!!!")

	return .option -> ret() where:
		ret = enable   if option == 'enable'   else \
			  disable if option == 'disable' else \
			  .-> print(f'No option called {option} => do nothing.')	  
