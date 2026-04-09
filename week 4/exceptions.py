""" 
try:
    x = int(input("What's x? "))
except ValueError:
    print("X is not an integer")

"""
#This throws a name error because x never gets a value if we dont provide an integer
#Since x never gets a value, and this line still tries to print x
# it throws a name error
# for it to not throw this error, we gotta put x inside the try catch block
# so that it doesn't get executed if it does catch an error
# in this case its gonna execute no matter what
#since its outside the try catch block
"""
print(f"Value is {x}")
"""


while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("Input the corect datatype (integer)")
        # pass (Just goes back)

print(f"Value is {x}")
