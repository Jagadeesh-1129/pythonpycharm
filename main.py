import random

# 1. Guess the Number Game!
secret_number = random.randint(1, 100)

print("Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations")


# 2. Scramble the word
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

word = random.choice(words)

print("Word Scramble Game!")

guess = ""
while guess != word:
    guess = input("Your guess: ")
    if guess == word:
        print("Correct!")
    else:
        print("Wrong, try again.")