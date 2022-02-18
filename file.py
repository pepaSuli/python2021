f = open("demofile.txt", "r")
print("szöveg")
print("szöveg2")
for x in f:
  print("-")
  print(x,end="")

f.close()
