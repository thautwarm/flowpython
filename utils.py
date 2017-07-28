def  createTemp(file:"filename of temp file"):
        if not os.path.exists(file):
            os.makedirs(file)
def isFileExists(file:"filename")-> "# Judge if source file exists and deal with the errors.":
        return True if os.path.exists(file) else FileNotFoundError(file)

def tryAction(string):
    try:
        return eval(string)
    except:
        return BaseException(string)

def fload(file):
    with open(file, encoding='gb18030') as f:
        s = f.read()
    return s

def fsave(source, file):
    with open(file, encoding='gb18030') as f:
        f.write(source)
    