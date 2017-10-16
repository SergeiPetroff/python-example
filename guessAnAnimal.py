from Node import *
from time import sleep
import Questions

##print( '\nClass Instances Of:\n' , Node.__doc__ )
print( '\n***Guess an Animal***')

firstAnimal = Node('Dragon')
secStopping = 3    

while True :
    pointer = firstAnimal
##    print( '\nCountOfNode\t' , Node.count )
    print( '\nThink an animal:)')
    sleep(secStopping)
           
    while pointer.isLeaf == False :
        print( '\nDoes it have such feature or characteristic as:' , pointer.mark , '?')
        user = input( '\n(Yes -> y, No -> n):  ' )
        user = Questions.checkInput(user) 
           
        if user == 'y' :
           pointer = pointer.knotLeft          
        elif user == 'n' :
           pointer = pointer.knotRight
            
    lastAnimal = pointer
    print( '\nIs it a', lastAnimal.animal , '?' )   
    user = input( '\nHave I guessed? (Yes! -> y, No:( -> n):  ' )
    user = Questions.checkInput(user) 
    
    if user == 'y' :
        print( '\nI win!' )
        
        if Questions.askContinueTheGame() == True :
            continue       
        else :
            break       
    elif user == 'n' :
        print( '\nI give in!' )
        userWho = input( '\nWho is it?: ')
        userWhat = input( '\nWhat is the difference from?  ')       
        newAnimalLeft = Node(userWho)
##        setattr(newAnimalRight , 'animal', getattr(lastAnimal , 'animal'))        
        newAnimalRight = Node(lastAnimal.animal)              
        lastAnimal.makeKnot(userWhat, newAnimalLeft, newAnimalRight)              
        print( '\nThank you for the hint.' )
       
        if Questions.askContinueTheGame() == True :
            continue       
        else :
            break            
