a,b = [],[]

def add(a,b):
    len_arr = len(a)
    if len(a) > len(b):
        len_arr = len(b)
    # print(len_arr)
    c = []
    for i in range(len_arr):
        c.append(a[i] + b[i])
    print(c)

def sub(a,b):
    len_arr = len(a)
    if len(a) > len(b):
        len_arr = len(b)
    # print(len_arr)
    c = []
    for i in range(len_arr):
        c.append(a[i] - b[i])
    print(c)

def main():
    n1 = int(input("Number of element in the array : ")) 
    for i in range(0,n1):
        global a
        i = int(input("Element of the array"))
        a.append(i)
    print(a)
    n2 = int(input("Number of element in the array : "))
    for i in range(0,n2):
        global b
        i = int(input("Element of the array"))
        b.append(i)
    print(b)
    choice = int(input("1]add\n 2]subract\n 3]multiply\n 4]exit"))
    match choice:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
main()
 