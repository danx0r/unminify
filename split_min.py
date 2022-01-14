import sys

f = open(sys.argv[1])
s = f.read()
for row in s.split(";"):
    print (f"{row};")
f.close()
