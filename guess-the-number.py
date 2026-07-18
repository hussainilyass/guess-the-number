import random

target=random.randint(1,100)

while True:
    user_choice=input("Enter Your target or quit:")

    if (user_choice=="quit"):
        print("target:",target)
        break

    if (int(user_choice)==target):
        print("----You Win----")
        print("Target: ",target)
        print("User choice: ",user_choice)
        break

    elif (int(user_choice)<target):
        print("----Your Target Is Small Try A Big Number----")

    else:
        print("----Your Target Is Big Try A Small Number----")

print("------GAME OVER------")