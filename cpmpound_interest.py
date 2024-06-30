amount = 0
def compound(p,t,r):
    amount = p*(pow((1+r/100),t))
    interest = amount - p
    return interest
p = float(input("enter the principal: "))
r = float(input("enter the rate: "))
t = float(input("enter the time: "))
print ("interest is ",compound(p,t,r))