# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = random.randint(0, 2)
if names == 0:
    print("Tom is going to buy the meal today!")
elif names == 1:
    print("Dick is going to buy the meal today!")
else:
    print("Harry is going to buy the meal today!")