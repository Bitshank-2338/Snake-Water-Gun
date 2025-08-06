import random
'''
-1 for snake
0 for water 
1 for gun
'''

computer=random.choice([-1,0,1])
you =input("Enter the choice:")
youDict={"s":-1,"w":0,"g":1}
reverseDict={-1:"Snake",0:"Water",1:"Gun"}

you=youDict[you]

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
    print("Its a Draw!")
else:
    if(computer==0 and you ==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    else:
        print("Something went wrong!")