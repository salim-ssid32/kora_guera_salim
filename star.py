import sys

# Check args len and type

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0])
    exit(-1)

n = 0

try:
    n = int(sys.argv[1])
except:
    print("Usage:", sys.argv[0])
    exit(-1)




