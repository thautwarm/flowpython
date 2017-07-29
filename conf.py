import os
import sys
if __name__ == '__main__':
    os.system("python config.py {}".format(' '.join(sys.argv[1:])))
    