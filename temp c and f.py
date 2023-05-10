

temp=int(input("enter temerature: "))
unit=str(input("enter unit F or C temerature: "))


if (unit=="f"):
    c=(temp-32)*(5/9)
    print("temerature in C ", c)
 
 
elif (unit=="c"):
    f=(temp*9/5)+32
    print("temerature in F " ,f)
     
else:
     print("try agin")
