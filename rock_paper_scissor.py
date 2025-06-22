import random

def user_choice():   
     while True:
        choice1=input("enter your option rock paper scissor :  ").lower()
        list=['rock' ,'paper',' scissor' ]
        if choice1 in list:
            return choice1
            break 
        else:
            print("please enter valid option")

            
def computer_option():
    choice2=str(random.choice(['rock' ,'paper',' scissor']))
    return str(choice2)


def winner(choice1,choice2):

    print(f"your choice {choice1} \ncomputer choice  {choice2}")
    if choice1==choice2:
        print("the game is draw ")
    elif choice1=='rock' and choice2=='scissor'or choice1=='paper' and choice2=='rock' or choice1=='scissor' and choice2=='paper':
        print("you won .....")
    else:
        print("computer won.... ")


while True:
   a= user_choice()
   b=computer_option()
   winner(a,b)
   play_agian=input("do you want to play again  yes /no : ").lower()
   
   if play_agian=='no':
       break
       

