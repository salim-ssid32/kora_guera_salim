import sys



def print_scare(n):
     #Made head
     print(" "*(n*3) + "*")
     for i in range(n -1):
          print(" "* (n*2) + " "*(n-i-1) + "*" + " "*((i+1)*2-1) + "*")

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

if n == 0:
     exit(0)


print_scare(n)



