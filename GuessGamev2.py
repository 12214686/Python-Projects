import random
import os
import time


print("\t___The Guess Game V2 ;)___\n\n")
x = input("Enter Your Name: ")

print(f"Hello {x}, Welcome to the guess Game")

time.sleep(1.2)



c = "y"


while c == "y":
    os.system("cls")
    a,b,c = str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))

    m = [a,b,c]
    #print(a,b,c)

    print("You have got 10 chances... choose wisely :)\n\n")

    count = 10
    while count != 0:
        x = input("Enter your three digit number: ")
        OhMyGawd = [i for i in x]

        l = []

        sa = 0
        for i in range(len(OhMyGawd)):
            if m[i] == OhMyGawd[i]:
                l.append("Correct")
                sa+=1
            else:
                l.append("Wrong")

        
        print()
        for i in l:
            print(i, end = " ")
        
        if sa == 3:
            print("\n\nYou Guessed them all right! ^-^ \n\n")
            break

        else:
            count-=1
            print(f"\n\nYou've got {count} chance(s) left !!!\n\n")
            time.sleep(1.5)
            os.system("cls")
        
        if count == 0:
            print(f"You were so close but the Answer was {m}")
            time.sleep(2.5)
            os.system("cls")

    
    print("\n\n")
    c = input("Want to Play Again (y/n)? ").lower()

    print("\n\nThank You for Playing :)...\n\n\nBye\n\n")
    os.system("pause")