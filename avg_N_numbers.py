num = int(input("How many numbers ?"))
total=0
for n in range (num):
    numbers = float(input("enter any number"))
    total = total +numbers
avg = total/num
print("avg is: ", avg)