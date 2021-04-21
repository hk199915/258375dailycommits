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

#Class
class Cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs

felix=Cat("ginger",4)
print(felix.color)

#Inheritence
class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky=Dog("Max","Grey")
husky.bark()

#Operator Overloading
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first=Vector2D(5,7)
second=Vector2D(3,9)
result=first+second
print(result.x)
print(result.y)

#Data Hiding
class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)

s=Spam()
s.print_egg()
print(s._Spam__egg)

#Class Methods
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def calculate_area(self):
        return self.width*self.height

    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)

square=Rectangle.new_square(5)
print(square.calculate_area())

#Static Methods
class Pizza:
    def __init__(self,toppings):
        self.toppings=toppings

    @staticmethod
    def validate_topping(topping):
        if topping=="pineapple":
            raise ValueError("No Pineapples!")
        else:
            return True

ingridients=["cheese","onions","spam"]
if all(Pizza.validate_topping(i) for i in ingridients):
    pizza=Pizza(ingridients)

#Regular Expressions
import re
pattern=r"spam"
if re.match(pattern,"eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern,"eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern,"eggspamsausagespam"))

import re
pattern=r"pam"

match=re.search(pattern,"eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

#Sub
import re
str="My name is David.Hi David"
pattern=r"David"
newstr=re.sub(pattern,"Amy",str)
print(newstr)

