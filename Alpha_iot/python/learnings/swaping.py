
def swap(a,b):
    temp = a
    a = b
    b = a
    return(a,b)
def main():
    n1 = int(input("Enter a number for n1: "))
    n2 = int(input("Enter a number for n2: "))
    n1,n2 = swap(n1,n2)
    print(f"The value of n1 is {n1} and for n2 {n2}")

main()