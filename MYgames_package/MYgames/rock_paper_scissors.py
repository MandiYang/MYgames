import random  #imports the random module to make random choices
alternatives = ['rock', 'scissors', 'paper'] #Create a list of weapons
play_again='yes'

#print out what computer choosed for weapon and what weapon you choosed.
def print_weapons(player1, player2):
    print(player1 + ':' + computer_ans + ' vs ' + player2 + ':' + answer)

if __name__=="__main__":
    while play_again=='yes' or play_again=='y':
    
        print('Welcome to my game, rock, scisscors and paper. \n' \
          'Choose your weapon below')
        
        computer_ans = random.choice(alternatives)
        
        answer = input('\n rock \n scissors \n paper \n: ') #Asking for weapons to use(answer)
        answer=answer.lower() #make the answer to lowercase letters, t.ex Rock is equally to rock
    
        #Define if it becomes tie
        if answer==computer_ans:       
            print_weapons('computer', 'you')
            print('tie')
    
        #Define if you loose    
        if (computer_ans=='rock'  and answer=='scissors') \
           or (computer_ans=='scissors' and answer=='paper') \
           or (computer_ans=='paper' and answer=='rock'):
            print_weapons('computer', 'you')
            print('you loose')
    
        #Define if you win
        if (computer_ans=='scissors' and answer=='rock') \
           or (computer_ans=='paper' and answer=='scissors') \
           or (computer_ans=='rock' and answer=='paper'):
            print_weapons('computer', 'you')
            print('you win')
    
        #Define if your answer is not valid
        elif (answer!='scissors') and (answer != 'rock') and (answer!='paper'): 
            print_weapons('computer', 'you')
            print('That\'s not a valid answer')
        
    
        play_again=input('play_again? yes/no: ')  #Ask to play agian(yes or no)    
