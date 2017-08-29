import os
def makedir_from(file):
    try:
        return os.path.split(file)[0]
    except:
        pass


def bin_copyto(file_from, file_to):
	render_dict =dict(file_from = file_from, file_to=file_to) 
	if not os.path.exists(file_from):
		raise BaseException("{file_from} not exists!".format(**render_dict))
	print("writing {file_from} to {file_to}...".format(**render_dict))
	with open(file_to, 'wb') as _to, open(file_from,'rb') as _from:
		_to.write(_from.read())

def moveto(file_from, file_to):
	render_dict =dict(file_from = file_from, file_to=file_to) 
	if not os.path.exists(file_from):
		raise BaseException("{file_from} not exists!".format(**render_dict))
	print("moving {file_from} to {file_to}...".format(**render_dict))
	os.rename(file_from, file_to)



