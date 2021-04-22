# Python3 code to demonstrate working of
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()

#initializing list
list_1=['futureskills','is','best']
list_2=['ratings','price','score']
list_3=[5,6,7]

#print original list
print("The original list 1 is:"+ str(list_1))
print("The original list 2 is:"+ str(list_2))
print("The original list 3 is:"+ str(list_3))

res=[{a:{b:c}} for(a,b,c) in zip(list_1,list_2,list_3)]

print("The constructed dictionary is:" + str(res))