slices=float(input("Enter number of slices you want:"))

if(slices%2==0):
    price=120.00*slices
    print("Total price:"+str(price))

else:
    price=123.00*slices
    print("Total price:"+str(price))