# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# Write your code below this line 👇

x_days = 365 * int(age)
y_weeks = 52 * int(age)
z_months = 12 * int(age)

x_days1 = 365 * 90
y_weeks1 = 52 * 90
z_months1 = 12 * 90

days = x_days1 - x_days 
weeks = y_weeks1 - y_weeks
months = z_months1 - z_months

print(f"You have {days} days, {weeks} weeks, and {months} months left.")