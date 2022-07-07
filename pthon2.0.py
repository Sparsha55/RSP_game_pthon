import random
lis = ["s", "p","r"]
chance = 3
no_of_chance = 0
your_point = 0
computer_point = 0

print("\t\t\t\t This is a rock scisor paper game. Lets play it\n")
print("Enter s for scisor.\nEnter r for rock.\nEnter p for paper.\n")

while(no_of_chance<chance):
    inputs = input("Scisor, Paper, Rock:")
    randoms = random.choice(lis)

    if(inputs == randoms):
        print("It's a tie. Try again")

    elif(inputs == "s" and randoms == "p"):
        your_point = your_point+1
        print(f"Your guess is {inputs} and computer guess is {randoms}.\n")
        print("You win one point\n")
        print(f"You made {your_point}and computer made {computer_point}\n")

    elif(inputs == "s" and randoms == "r"):
        computer_point = computer_point+1
        print(f"Your guess is {inputs} and computer point is {randoms}\n")
        print("Computer wins one point\n")
        print(f"You made {your_point} and computer made {computer_point}\n")

    elif (inputs == "p" and randoms == "s"):
        computer_point = computer_point + 1
        print(f"Your guess is {inputs} and computer guess is {randoms}.\n")
        print("Computer win one point\n")
        print(f"You made {your_point}and computer made {computer_point}\n")

    elif (inputs == "p" and randoms == "r"):
        your_point = your_point + 1
        print(f"Your guess is {inputs} and computer guess is {randoms}.\n")
        print("You win one point\n")
        print(f"You made {your_point}and computer made {computer_point}\n")

    elif (inputs == "r" and randoms == "s"):
        your_point = your_point + 1
        print(f"Your guess is {inputs} and computer guess is {randoms}.\n")
        print("You win one point\n")
        print(f"You made {your_point}and computer made {computer_point}\n")

    elif (inputs == "r" and randoms == "p"):
        computer_point =computer_point + 1
        print(f"Your guess is {inputs} and computer guess is {randoms}.\n")
        print("Computer win one point\n")
        print(f"You made {your_point}and computer made {computer_point}\n")

    else:
        print("It's a wrong input darling:\n")

    no_of_chance = no_of_chance+1

    print(f"{no_of_chance} have been played out of {chance}!\n")

print("GAME OVER")

if(computer_point == your_point):
    print("It is a tie\n")

elif(your_point<computer_point):
    print("You loose, sucker:\n")

else:
    print("Enjoy the victory, you win\n")







