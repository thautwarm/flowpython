import os

joinPath = os.path.join
def makedir(file):
    try:
        os.makedirs(file[:file.rfind("/")+1])
    except:
        pass
def  createTemp(file:"filename of temp file"):
        if not os.path.exists(file):
            makedir(file)
def isFileExists(file:"filename")-> "# Judge if source file exists and deal with the errors.":
        return True if os.path.exists(file) else FileNotFoundError(file)

def tryAction(string):
    try:
        return eval(string)
    except:
        return BaseException(string)

def fload(file):
    if not os.path.exists(file):
        print(Warning("{} does not exists.".format(file)))
        return 
    with open(file, encoding='gb18030') as f:
        s = f.read()
    return s

def fsave(source, file):
    if not source: return 
    if not os.path.exists(file):
        print(Warning("{} does not exists. create the file now...".format(file)))
        makedir(file)
    with open(file,'w', encoding='gb18030') as f:
        f.write(source)
    