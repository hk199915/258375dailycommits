# Python code to convert into dictionary using setdefault() method

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))


# Python code to convert into dictionary using dict() method
def Convert(tup, di):
    di = dict(tup)
    return di


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))

