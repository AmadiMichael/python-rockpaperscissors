import random

options = ['Rock', 'Paper', 'Scissors']
compPick = random.choice(options)
yourPick = input ('What is your take, Rock, Paper or Scissors')

print ('You chose ' + str.capitalize(yourPick.replace(" ", "")))
print('Computer chose ' + compPick)




if (yourPick == 'Rock') : 
    if (compPick == 'Rock'): 
        print ("It's a TIE!")
    if (compPick == 'Paper'): 
        print ("You LOSE!!")
    if (compPick == 'Scissors'): 
        print ("You WIN!")

if (yourPick == 'Paper') : 
    if (compPick == 'Rock'): 
        print ("You WIN!")
    if (compPick == 'Paper'): 
        print ("It's a TIE!")
    if (compPick == 'Scissors'): 
        print ("You LOSE!!")

if (yourPick == 'Scissors') : 
    if (compPick == 'Rock'): 
        print ("You LOSE!!")
    if (compPick == 'Paper'): 
        print ("You WIN!")
    if (compPick == 'Scissors'): 
        print ("It's a TIE!")


