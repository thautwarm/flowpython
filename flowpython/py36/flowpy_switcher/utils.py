import os
def makedir_from(file):
    try:
        return os.path.split(file)[0]
    except:
        pass


def bin_copyto(file_from, file_to):
	if not os.path.exists(file_from):
		raise BaseException(f"{file_from} not exists!")
	print(f"writing {file_from} to {file_to}...")
	with open(file_to, 'wb') as _to, open(file_from,'rb') as _from:
		_to.write(_from.read())

def moveto(file_from, file_to):
	if not os.path.exists(file_from):
		raise BaseException(f"{file_from} not exists!")
	print(f"moving {file_from} to {file_to}...")
	os.rename(file_from, file_to)



