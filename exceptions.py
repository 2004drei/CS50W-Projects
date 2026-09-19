import sys


try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("Cannot divide strings, IDIOT!")
  sys.exit(1)

try:
  result = x / y
except ZeroDivisionError:
  print("You can't divide by zero, IDIOT!")
  sys.exit(1)