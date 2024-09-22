prev1,prev2 = 0,1

def fib_series(n):
    if n<1 or n == 1:
        print(0)
        return 0
    elif n==2:
        print(0,1)
        return 0
    else:
        print(0)
        print(1)
        fib(n)
        
def fib(n):
    global prev1,prev2
    if n<3:
        return
    next = prev1 + prev2
    prev1 = prev2
    prev2 = next
    print(next)
    return fib(n-1)

def main():
    n = int(input("Enter the number of patters :"))
    fib_series(n)

main()
