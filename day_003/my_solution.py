# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

result_1 = year / 4
result_2 = year / 100
result_3 = year / 400

if result_1 == int(result_1):
    print("Leap year.")
elif result_1 == float(result_1):
    print("Not leap year.")

elif result_2 == int(result_2):
    print("Not leap year.")
elif result_2 == float(result_2):
    print("Leap year.")

elif result_3 == int(result_3):
    print("Leap year.")
elif result_3 == float(result_3):
    print("Not leap year")
else:
    pass