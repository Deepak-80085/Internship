#To calculate the number of days, months, and years between the birthdate and the current date.
from datetime import date

def check_birthdate():
    while True:
        try:
            data = input("Enter your birthdate in YYYY-MM-DD format: ")  # Prompt user to enter birthdate
            birthdate = date.fromisoformat(data)  # Convert input string to date object
            if birthdate <= date.today():  # Check if birthdate is valid or in the past
                return birthdate
            else:
                print("Invalid date. Please enter a valid or past date.")  # Display error message for invalid future date
        except ValueError:
            print("Invalid input.")  # Display error message for invalid input format

def check(birthdate):
    today = date.today()
    no_of_days = (today - birthdate).days  # Calculate the number of days between birthdate and today
    years = no_of_days // 365  # Calculate the number of years
    no_of_months = (no_of_days) // 30  # Calculate the number of months
    print("Number of days:", no_of_days)  # Display the number of days
    print("Number of months:", no_of_months)  # Display the number of months
    print("Number of years:", years)  # Display the number of years

def main():
    birthdate = check_birthdate()  # Get the birthdate from user
    check(birthdate)  # Calculate and display the number of days, months, and years

main()  # Call the main function