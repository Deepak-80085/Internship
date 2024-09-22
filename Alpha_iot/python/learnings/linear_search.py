def linear():
    # Create an empty array
    array = []
    while True:
        try:
            # Get the number of elements for the array from the user
            number = int(input("Enter the number of elements for the array: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    for i in range(number):
        # Get each element from the user and append it to the array
        element = input("Enter element: ")
        array.append(element)
    print(array)
    return array

def indexValue():
    # Get the array from the linear() function
    array = linear()
    while True:
        try:
            # Get the index value from the user
            index = int(input("Enter the index value: "))
            # Print the element at the given index
            print(array[index])
            break
        except (ValueError, IndexError):
            print("Invalid index. Please enter a valid integer within the range of the array.")

def elementValue():
    # Get the array from the linear() function
    array = linear()
    while True:
        try:
            # Get the number from the user
            element = (input("Enter the element: "))
            if element in array:
                # Find the index of the element in the array and print it
                index = array.index(element) 
                print(index)
                break
            else:
                print("Element not found in the array.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Linear Search")
    while True:
        try:
            # Get the option from the user
            print("-------------------------------------------------------------------------------------------")
            option = int(input("1] To find the element from the index\n2] To find the index from the element\nEnter 1 or 2: "))
            if option == 1:
                # Call the indexValue() function if option is 1
                indexValue()
            elif option == 2:
                # Call the numberValue() function if option is 2
                elementValue()
            else:
                print("Invalid option. Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()