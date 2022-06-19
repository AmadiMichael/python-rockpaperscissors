import random



options = ['Rock', 'Paper', 'Scissors']
compPick = random.choice(options)
yourPick = input ('What is your take, Rock, Paper or Scissors')

    
print ('You chose ' + str.capitalize(yourPick.replace(" ", "")))
print ('Computer chose ' + compPick)




if (yourPick == 'Rock') : 
        if (compPick == 'Rock'): 
            print ("It's a TIE!")
        elif (compPick == 'Paper'): 
            print ("You LOSE!!")
        else: 
            print ("You WIN!")

elif (yourPick == 'Paper') : 
        if (compPick == 'Rock'): 
            print ("You WIN!")
        elif (compPick == 'Paper'): 
            print ("It's a TIE!")
        else: 
            print ("You LOSE!!")

elif (yourPick == 'Scissors') : 
        if (compPick == 'Rock'): 
            print ("You LOSE!!")
        elif (compPick == 'Paper'): 
            print ("You WIN!")
        else: 
            print ("It's a TIE!")
