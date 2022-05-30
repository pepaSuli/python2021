import smsmodul

f=open("sms.txt")
sorok=f.read().split("\n")[1:-1]
f.close()


print(sorok)

for i in range(0:len(sorok)/2):
    pass
