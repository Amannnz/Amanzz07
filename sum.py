import sys 
s=0
for i in range (1, len(sys.argv)):
      s = s+ int(sys.argv[i])
print(f"sum is {s}")
