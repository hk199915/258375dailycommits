print("Hello World")
print("Second Commit")

print(None)

ages={"Dave":24,"Marry":42,"Jhon":58}
print(ages["Dave"])
print(ages["Marry"])

squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#string formatting
nums=[4,5,6]
msg="Numbers:{0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)

#lambda function
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

#map function
def add_five(x):
    return x+5

nums=[11,22,33,44,55]
result=list(map(add_five,nums))
print(result)