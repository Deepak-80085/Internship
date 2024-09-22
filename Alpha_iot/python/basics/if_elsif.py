n = int(input("Enter a number : " ))
if (n<10):
    print("It is a single digit number")
elif (n<100):
    print("It is a double digit number")
elif(n<1000):
    print("It is a three digit number")
else:
    print("It is either four or greater than four digit number")