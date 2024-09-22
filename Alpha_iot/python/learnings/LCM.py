def main():
    x = int(input("Enter  x : "))
    y = int(input("Enter  y : "))
    max = 0     
    if x>y:
        max = x
    else:
        max = y
    while True:
        if max%x == 0 and max%y == 0:
            print(f"The LCM is {max}")
            break
        max = max + 1

main()