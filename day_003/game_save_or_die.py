print('''
*******************************************************************************
                   /\\
                  /  \\
                 /    \\
                /------\\
               / |    | \\
              /  |____|  \\
             /  /      \\  \\
            /  /        \\  \\
           /  /__________\\  \\
          /  /            \\  \\
         /  /              \\  \\
        /  /                \\  \\
       /  /                  \\  \\
      /  /____________________\\  \\
     /  /|    ________          |\\  \\
    /  / |   /  O  O  \\         | \\  \\
   /  /  |  |    ()    |        |  \\  \\
  /  /   |   \\ ______ /         |   \\  \\
 /  /    \\   /        \\         /    \\  \\
/__/      \\_/__________\\_______/      \\__\\
*******************************************************************************
''')
print("Welcome to Save or Die.")
print("Your mission is to find the Princess.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

player_choice = input("You are in a middle of a forest and you are in a hurry to save the Princess! Where do you go, 'Left' or 'Right' ?")
player_choice = player_choice.lower()

if player_choice == "left":
    river_choice = input("Well done! You have reached the river, what do you do 'Wait' or 'Swim'? ")
    if river_choice == "swim":
        castle_choice = input("It's high risk high reward but you have done it! Now you are running in the castle and you are in a big room with 3 doors... which door do you open...'Red', 'Yellow', 'Green' or turn around and run for your life ?" )
        if castle_choice == "green":
            print("Green color it's not always good, you've opened room full of toxic green gas! You have DIED !")
        elif castle_choice == "yellow":
            print("You are not lucky, you opened a room with big yellow-eyed dragon and you cannot deffend yourself! You have DIED !")
        elif castle_choice == "run":
            print("Didn't expect that...GAME OVER !!!")
        else:
            print("You have done it! You saved the Princess! If you play your cards right, she could sleep with you !")
    else:
        print("You've waited too long, wolfs are nearby and they are hungry! Sorry, you have DIED !")
else:
    print("Sorry ,there was a trap pit hole. You have DIED !")
