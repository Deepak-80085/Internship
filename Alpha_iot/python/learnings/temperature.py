print("Convert Celsius into Kevlin or Fahrenheit")
while True:
    check = int(input("1) Kelvin or 2) Fahrenheit 3)exit: "))
    if(check >=3):
        break
    cel = int(input("Enter the temperature value in celsius : "))
    match check:
        case 1:
            print("The temperature in kelvin is ",cel+273.5)
        case 2:
            print("The temperature in Fahrenheit is : ",(cel*(9/5)+32))