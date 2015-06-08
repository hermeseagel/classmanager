import os.path
print(os.path.dirname(__file__))

dirname = os.path.dirname(os.path.dirname(__file__))
realpath = os.path.dirname(os.path.realpath(__file__))
abspath = os.path.dirname(os.path.abspath(__file__))

#print(dirname)
print(realpath)
#print(abspath)
