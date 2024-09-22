import random
def main():
    # The user enters a valid range (start and end values), and the program generates a random number within that range. The user then tries to guess the number, based on their guesses.
    print("------- To guess a number ---------")
    while True:
        try:
            lower_range = valid_int("Enter the starting number for the range: ")
            upper_range = valid_int("Enter the ending number for the range: ")
            # Validate range (start must be less than or equal to end)
            if lower_range > upper_range:
                print("Invalid range: Starting number must be less than or equal to ending number.")
                continue
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    random_number = 0
    while random_number == 0:
        random_number = random.randint(lower_range, upper_range)
     # Calculate maximum guesses based on range
    max_guesses = upper_range - lower_range + 1 
    count = 0  # Initialize guess counter
    guess_no = 0
    while count < max_guesses and guess_no != random_number:
        guess_no = valid_int(f"Enter a number between {lower_range} and {upper_range}: ")

        # Provide hints and increment guess count
        if guess_no < lower_range or guess_no > upper_range:
            print(f"Invalid guess. Please enter a number between {lower_range} and {upper_range}.")
        elif guess_no > random_number:
            print("You guessed higher. Try again.")
        elif guess_no < random_number:
            print("You guessed lower. Try again.")
        count += 1
        
    # win or lose 
    if guess_no == random_number:
        print(f"Congratulations! You guessed the number {random_number} correctly in {count} guesses.")
    else:
        print(f"Sorry, you ran out of guesses. The number was {random_number}.")


def valid_int(prompt):
    # Prompts the user for a valid integer input and returns it.

    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
main()

