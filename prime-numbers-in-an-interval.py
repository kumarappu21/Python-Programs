m = int(input("first number of the interval: "))
n = int(input("second number of the interval: "))
for a in range (m,n+1):
    if a>1:
        for i in range(2,a):
            if a%i ==0:
                break
        else:
            print(a)