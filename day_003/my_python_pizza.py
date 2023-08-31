# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
lager_pizza = 25

pepperoni_s = 2
pepperoni_m = 3
pepperoni_l = 3
cheese = 1

bill = 0

if size == "S":
    bill += small_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_s
    else:
        if extra_cheese == "Y":
            bill += cheese

if size == "M":
    bill += medium_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_m
        if extra_cheese == "Y":
            bill += cheese

if size == "L":
    bill += lager_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_l
        if extra_cheese == "Y":
            bill += cheese
print(f"Your final bill is: ${bill}.")
