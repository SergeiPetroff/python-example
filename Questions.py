def checkInput(userInput) :
    user = userInput
    while not(user == 'y' or user == 'n') :
        user = input( '\nPlease, repeat the response. (Yes! -> y, No:( -> n):  ')
    return user

def askContinueTheGame() :  
    user = input( '\nDo you want to continue the game? (Yes! -> y, No:( -> n):  ' )   
    user = checkInput(user) 
        
    if user == 'y' :
        return True       
    elif user == 'n' :
        print( '\nThe game is over!' )
        return False 
