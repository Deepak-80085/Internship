print("----------TO CHECK YEAR IS A LEAP YEAR----------")
x = int(input("Enter a year : "))
leap_year = x%4
if (leap_year == 0):
    print(x," is a leap year")
else:
    print(x,"is not leap year")