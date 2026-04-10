# To save the names permanently in a .txt file

name = input("Gimme a name: ")

with open("file.txt", "a") as file: # Prevents the usage of file.close() as it has its own scope
    file.write(f"{name}\n")                # "a" is for appending and "w" is for overwriting
# with itself doesn't have its own scope(functions and classes do), however after the with statement, the file closes automatically as it wipes it from the memory
