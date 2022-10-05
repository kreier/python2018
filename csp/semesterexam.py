def is_even(number):
  if type(number) != int:
    print("Must be an integer!")
    return -1
  if number % 2 == 0:
    return True
  else:
    return False

x = int(input("Enter a number: "))


if is_even(x):
  print("Your number is even.")
else:
  print("Your number is odd.")
