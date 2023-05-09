
# cost and vat of tans of iron, one tans= 1 rial

ton=int(input("enter ton of iron: "))
vat=int(input("enter vat % of iron: "))

cost= 1 * ton

vatpr = cost *(vat/100)

total= cost + vatpr

print("cost of iron is: ",cost)
print("vat is: ",vatpr)
print("total cost is:",total)
