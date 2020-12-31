n=int(input("Enter n:"))
i=0
a=0
b=1
c=0
while i<n:
    if i==(n-1):
        print(c)
        break
    if i==2:
        print("1",end=",")
        i+=1
        continue
    print(c,end=",")
    c=a+b
    a=b
    b=c
    i+=1
