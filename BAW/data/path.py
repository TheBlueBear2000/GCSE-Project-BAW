import os
import sys

directdir = os.path.dirname(os.path.realpath(sys.argv[0]))

dir = directdir[:len(directdir) - 4]

print(dir + ", " + str(type(dir)))

