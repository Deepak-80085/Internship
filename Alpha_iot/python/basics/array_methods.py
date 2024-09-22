print("-------------------ARRAY METHODS-----------------------")
a = []
x = 0 
while(x!=11):
            print("\n\n1]  append \n2]  clear \n3]  copy \n4]  count \n5]  extend \n6]  index \n7]  insert \n8]  pop \n9]  reverse \n10] sort \n11] exit")
            x = int(input("Enter a choice : "))
            match x :
                case 1:
                    i = int(input("Enter element : "))
                    a.append(i)
                    print(a)
                case 2:
                    a.clear()
                    print(a)
                case 3:
                    z = a.copy()
                    print(z)
                case 4:
                    print(a)
                    c = int(input("Enter element to count : "))
                    q = a.count(c)
                    print(q)
                case 5:
                    ex = []
                    n = int((input("Enter the number of elements to extend : ")))
                    for i in range(n):
                        i = int(input("Enter element : "))
                        ex.append(i)
                    print("New array : ",ex)
                    a.extend(ex)
                    print("Array after extending",a)
                case 6:
                    print(a)
                    x = int((input("Enter the element : ")))
                    index = a.index(x)
                    print('The index is :',index)
                case 7:
                    i = (input("Enter the index : "))
                    x = ((input("Enter element to be added : ")))
                    a.insert(i,x)
                    print(a)
                case 8:
                    i = int(input("Enter the index : "))
                    a.pop(i)
                    print(a)
                case 9:
                    print(a)
                    a.reverse()
                    print(a)
                case 10:
                    a.sort()
                    print(a)
                case 11:
                    exit