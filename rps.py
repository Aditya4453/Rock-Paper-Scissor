import random
print("1. Rock \n 2. Paper \n 3. Scissor")

def rockpaperscissor(n):
    user_score=0
    comp_score=0
    for i in range(n):
        user_input=int(input("Enter your input :"))
        comp_input=random.choice([1,2,3])
        print("User Input :",user_input)
        print("Computer Input :",comp_input)
        if user_input==comp_input:
            continue
        elif user_input == 2 and comp_input==1 :
            user_score+=1
        elif user_input==1 and comp_input==3:
            user_score+=1
        elif user_input==3 and comp_input==2:
            user_score+=1
        else:
            comp_score+=1
    if user_score>comp_score:
        return True
    elif user_score==comp_score:
        print(" - - - - - - -  \nBogee ho gaya yaar \none more chance to decide \n - - - - - - - ")
        rockpaperscissor(1)
    else:
        return False

n=int(input("Enter no of chances :"))
result = rockpaperscissor(n)
if result==True :
    print(" - - - - - - -  \nUser Wins \n - - - - - - - ")
else :
    print(" - - - - - - -  \nComputer Wins \n - - - - - - - ")
