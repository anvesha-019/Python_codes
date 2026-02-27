# Q7) Write a program for employee bonus calculation. If the employee has completed more than equal to 5 years in the company, then he will get a bonus of 10% of his salary, if the same employees salary is less than Rs. 50000 then he will get a bonus of 5% of his salary.

salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the number of years the employee has completed in the company: "))
if years_of_service >= 5:
  if salary < 50000:
    bonus = salary * 0.05
  else:
    bonus = salary * 0.10
else:  bonus = 0
print("The employee's bonus is: Rs.", bonus)