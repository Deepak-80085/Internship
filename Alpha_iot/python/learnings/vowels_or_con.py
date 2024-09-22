#To check the given word has vowels or consonants
def check(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    countOfVowel,countOfCon = 0,0  # Initialize count variable
    for i in word:
        if i in vowels:  # Check if the character is a vowel
            countOfVowel += 1  # Increment count by 1
        if i not in vowels:
            countOfCon += 1   
    print(f"Number of vowels is {countOfVowel} and number of consonants is {countOfCon} in '{word}'.")

def main():
    while True:
            word = input("Enter an word: ")# Prompt the user to enter a word
            if word.isalpha():
                check(word.lower())  # Check if the word has a vowel or a consonant
            else:
                print("Invalid input. Please enter a valid word.")
                continue
            break
        
main()