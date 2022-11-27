import random
game=["snake","water","gun"]
chances=0
Your_points=0
My_points=0
while chances<10:
    choice = random.choice(game)
    print("choose one of them::", ["snake", "water", "gun"])
    you = str(input("Your choice::"))
    print("my choice:", choice)
    if you=="snake" and choice=="snake":
        print("Tie")
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="water" and choice=="water":
        print("Tie")
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="gun" and choice=="gun":
        print("Tie")
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="snake" and choice=="water":
        print("you win")
        Your_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="snake" and choice=="gun":
        print("you lost")
        My_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="water" and choice=="gun":
        print("you win")
        Your_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="water" and choice=="snake":
        print("You lost")
        My_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="gun" and choice=="snake":
        print("you win")
        Your_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    elif you=="gun" and choice=="water":
        print("You lost")
        My_points+=1
        print("your points:",Your_points)
        print("MY points:",My_points)
        chances+=1
        print("NO of chances are left:",9-chances)
    else:
        print("")
if Your_points>My_points:
    print("YOU POINTS:",Your_points,"YOUR WINNR")
elif My_points>Your_points:
    print("YOU POINTS:",My_points,"YOUR LOSSER")
elif Your_points==My_points:
    print("Game Tie")
else:
    print("GAME OVER!!")
