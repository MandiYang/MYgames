def control(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print('Right answer!')
        score += 1
    else:
        print("Wrong answer, the answer is " + answer)
score = 0

if __name__=='__main__':
    print('Guess the animal!')
    
    guess1 = input('Which animal has 4 legs and has a very long throat? : ')
    control(guess1, 'giraff')
    guess2 = input('What is the most fastest animal on land?:  ')
    control(guess2, 'cheetah')
    guess3 = input('What is the biggest animal in the world?:  ')
    control(guess3, 'blue whale')
    guess3 = input('What is the name of the smartest animal?:  ')
    control(guess3, 'human')

    print('Your total score is ' + str(score))

    if score>2:
        print('Good job! You are a genius :)')
        
