import sys

f = open(sys.argv[1])
for row in f.readlines():
    if row[-1] == "\n":
        row = row[:-1]
    sys.stdout.write(row)

f.close()

