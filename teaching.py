# for the homework, define all the functions at the top of the file and then call them all at the bottom

# defining the function, named as a VERB
# this one returns a value, which you can then do stuff with
def make_list(value, multiplier):
    multiplied_string = str(value) * multiplier
    return multiplied_string


# this just prints it but you'd have to call it repeatedly to do multiple things, less efficient
def print_list(value, *, multiplier):
    multiplied_string = str(value) * multiplier
    print(multiplied_string)


# this is not returning something, but it is modifying an existing list
def change_list(input_list, value, multiplier):
    input_list.append(str(value) * multiplier)

names = ["Mya"]
print(names)
change_list(names, "hello ", 2)
print(names)

# call this function
# option 1, create a variable to store the returned value (most common)

message = make_list("Jody ", 6)
print(message)

# option 2, call the function within another function
print(make_list("Spam ", len("Spam")))
print(make_list("Spam ", 4))

spam_string = make_list("Spam ", 3)
print(spam_string)

# only option for a function without a return
print_list("Everyone ", multiplier=3)

# calling with named paramaters
print_list(multiplier=3, value="Boo! ")
print_list(value="Hello! ", multiplier=2)

# passing positionally
print_list("bOO!", multiplier=4)