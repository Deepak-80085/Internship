
def primenumbers(n):
    for a in range(2, n//2):
        if n % a == 0:
            return False 
    return True 

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print(f"Prime numbers between {n1} and {n2} are: ")
for i in range(n1, n2 + 1):
    if primenumbers(i):
        print(f"| {i}",)
    