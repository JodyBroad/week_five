# practice!

def make_list(val, times):
    res = str(val) * times
    return res

print(make_list("hello ", 6))

def print_list(val, times):
    print(str(val) * times)

print_list(5, 3)
print_list(0, 4)

def change_list(inlist, val, times):
    inlist += str(val) * times
mylist = []
change_list(mylist, "h", 8)
print(mylist)


def print_vat(gross, vatpc=17.5, message="Summary: "):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))

print_vat(9.55)

print_vat(9.55, message="Final sum:")

def my_func(file, dir, user="root"):
    print("file: {:}, dir: {:}, to: {:}".format(file, dir, user))

my_func("one", "two", "three")

my_func("one", "two")

my_func(file="one", user="three", dir="two")