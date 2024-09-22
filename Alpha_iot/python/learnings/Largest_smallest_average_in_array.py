a = []
def largest(a):
    print(a)
    max = 0
    for i in a:
        if(max < i):
            max = i
    print("The largest element in the array is",max)
    for i in a:
        if(max > i):
            max = i
    print("The smallest element in the array is",max)
def average(n,a):
    av = 0
    for i in a:
        av += i
    av = av/n
    print("Average of the array in element : ",av) 

def main():
    n = int(input("ENter the numbers the elements in the array :")) 
    for i in range(0,n):
        i = int(input(f"ENter the element {i} :"))
        global a 
        a.append(i)
    largest(a)
    average(n,a)

main()