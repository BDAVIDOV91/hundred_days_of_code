#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	
#Write the rest of your code below this line 👇

toss_coin = random.randint(0, 1)

if toss_coin == 1:
    print("Heads")
else:
    print("Tails")