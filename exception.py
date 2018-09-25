import random
print("Hello what is your name ?")
name = input()
SecretNumber=random.randint(1,20)
print("Well," + name +  "I am thinking of a number between 1 and 20")

# Asking players to take a guess

for guesstaken in range(1,7):
     print("Take a guess")
     guess = int(input())
     if guess < SecretNumber:
          print("Your guess is too low")
     elif guess > SecretNumber:
          print("Your guess is too high")
     else:
          break

if guess == SecretNumber:
     print("Good job, " + name + "You guessed my number in ," + str(guesstaken) + "guesses")
else:
     print("Nope. The number i was thinking of was " + str(SecretNumber))
          
     


