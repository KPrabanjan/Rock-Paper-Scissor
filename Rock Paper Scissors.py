import random
Play="Y"
while Play=="Y":
    game=['rock', 'paper', 'scissor']
    comp_choice=random.choice(game)
#choice from user
    Input=input("CHOOSE ONE [rock,paper,scissor]:")
#tie
    if comp_choice==Input:
        print("Tie")
#not a tie
    elif comp_choice!=Input:
#comp chooses rock
        if comp_choice=="rock":
            if Input=="scissor":
                print("User Out")
            else:
                print("Computer Out")
#comp chooses paper
        elif comp_choice=="paper":
            if Input=="rock":
                print("User Out")
            else:
                print("Computer Out")
#comp chooses scissor
        elif comp_choice=="scissor":
            if Input=="paper":
                print("User Out")
            else:
                print("Computer Out")
        
#wrong input        
    else:
        print("Invalid choice, Try Again!")
    print("You: ", Input)
    print("Computer: ", comp_choice)
    Play=input("Play Again?(Y/N):")
    
