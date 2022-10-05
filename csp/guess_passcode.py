"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()
# Write your code here

print("Is Random faster? Let's run this 100 times!\n")
nr_random = 0
nr_sequence = 0
nr_notfound = 0
for cycle in range(100):
  secret_passcode = generate_random_passcode()
  for i in range(50000):
      x = random.randint(0, 9999)
      if is_correct(str(x), secret_passcode):
          print(".", end='')
          break  
  if i == 49999:
      nr_notfound += 1
  else:
    if x > i:
        nr_random += 1
    else:
        nr_sequence += 1

print("\nResults:")
print('Could not crack it:    ' + str(nr_notfound) + ' times.')
print('Random was faster:     ' + str(nr_random) + ' times.')
print('Sequential was faster: ' + str(nr_sequence) + ' times.')
