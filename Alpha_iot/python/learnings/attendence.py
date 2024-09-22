reg_no = int(input("Enter your regsister number : "))
if(reg_no<0):
    print("Invalid regsister number")
    exit(0)

total_class = int(input("Enter your total classes held :"))
attended = int(input("Enter the number of classes attended : "))
if(attended > total_class):
    print("Invalid values")
    exit(0)
percentage = (attended/total_class)*100
print(percentage)
if(percentage<75):
    print("Due to shortage of attendence fine of amount $69 should be paid")
elif(percentage<85):
    print("Credit 3")
elif(percentage<90):
    print("Credit 4")
else:
    print("Credit 5")
