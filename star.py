import sys

# Check args len

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0])
    exit(-1)

n = 0

# Check n type
try:
    n = int(sys.argv[1])
except:
    print("Usage:", sys.argv[0])
    exit(-1)

# Check n is positive
if n < 0:
        print("Usage:", sys.argv[0])
        exit(-1)




