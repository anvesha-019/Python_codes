#Q1) Write a program to check whether the given number is positive.

n= int(input("Enter the number: "))
if n > 0:
  print("The number is positive.")
elif n == 0:
  print("The number is zero.")
else:
  print("The number is negative.")