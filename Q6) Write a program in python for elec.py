# Q6) Write a program in python for electricity bill calculation. For 1st 100 units Rs. 3/unit, for next 100 units Rs. 5/unit and for above 200 units Rs. 7/unit.

units = int(input("Enter the number of units consumed: "))
if units <= 100:
  bill = units * 3
elif units <= 200:
  bill = (100 * 3) + ((units - 100) * 5)
else:
  bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)
print("Your electricity bill is: Rs.", bill)