import random
import math
import time
import sys

'''
Authors: Lakshman Chelliah, Dylan Dominic
Version 0.0.2
Date: 2023-03-08
'''

import sys

# Define the different colors
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    REDB = '\033[1;91m'
    REDBB = '\033[38;5;124m'
    RED = '\033[0;31m'
    CYAN = '\033[0;36m'
    CYANB = '\033[1;96m'
    GREENB = '\033[48;5;22m'
    END = '\033[0m'

#colors.RED + "Invalid Input" + colors.END

#How many Decks there are
SHOE_SIZE = 6
#Max number the dealer will hit on
DEALER_HIT_ON = 16

#Creates BlackJack Shoe with SHOE_SIZE amount of decks 
def makeShoe()->list:
    deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    symbols = ["♠","♥","♦","♣"]
    
    finaldeck = [];

    for x in symbols:
        for y in deck:
            finaldeck.append(str(x) + str(y))
    #Creates *SHOE_SIZE* amount of decks
    finaldeck = finaldeck*SHOE_SIZE
    random.shuffle(finaldeck)
    
    return finaldeck


#Converts Cards in Hand to a Value to be compared with opponent 
#Looks at Number of "A" and determines when the best value with n Aces
def checkScore(hand) -> int:
    score = 0
    aceCount = 0
    
    for card in hand:
        #Takes the last character of the card and determines if its value
        temp = card[-1]
        if (temp == "J" or temp == "Q" or temp == "K"):
            score+=10
        elif (temp != "A"):
            if (temp=="0"):
                score +=10
            else:
                score = score + int(temp)
        else:
            score+=11
            aceCount += 1
            
    #If the value is greater than 21 and there are aces present
    #subtract 10 from the count to make the aces represent 1 instead of 11        
    while score > 21 and aceCount > 0:
        score -= 10
        aceCount -= 1
            
    return score
    
    
#Made for Player
#Gives another card until not needed
def hitCard (hand, deck)->bool:
    #Initial HIT
    hand.append(deck.pop())
    print(colors.CYANB+"Player Cards"+colors.END)
    print(colors.CYAN+str(hand) + " -> " + str(checkScore(hand))+colors.END)

    #Lets player keep HITting until they STAND
    while True:
        if (checkScore(hand) > 21):
            return False
        else:
            userIn = input('What would you like to do?\n-\'H\'it -\'S\'tand   : ')
            if (userIn.upper() == 'H'):
                return True
            elif (userIn.upper() == 'S'):
                return False
            else:
                print(colors.REDBB+"Invalid Input"+colors.END)
                userIn = input('What would you like to do?\n-\'H\'it -\'S\'tand   : ')


#Dealer's Version of hitCard
#Dealer will hit on DEALER_HIT_ON
def dealerTurn(hand, deck)->None:
    
    print(colors.REDB+"Dealers Cards"+ colors.END)
    print(hand)
    
    while (checkScore(hand) <= DEALER_HIT_ON):
        print(colors.REDB+"Dealer HIT"+ colors.END)
        time.sleep(3)
        hand.append(deck.pop())
        print(hand)
        time.sleep(3)
      
        
#Evalutes round and returns:
#1 for Player 
#-1 for Dealer
#0 for Tie
#2 for Blackjack
def evalRound(player, dealer)->int:
    
    #Check if player or dealer busts
    playerBust = checkScore(player) > 21
    dealerBust = checkScore(dealer) > 21

    playerCount = checkScore(player) 
    dealerCount = checkScore(dealer)
    
    print('\n')
    #If Dealer busts
    if (dealerBust and not playerBust):
        print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
        print(colors.GREENB+"DEALER BUST"+ colors.END)
        print(colors.GREENB+"YOU WON"+colors.END)
        return 1
    #If Player busts
    elif (playerBust and not dealerBust):
        print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
        print(colors.REDBB+"YOU BUST"+colors.END)
        print(colors.REDBB+"YOU LOST"+colors.END)
        return -1
    #If both busts
    elif (playerBust and dealerBust):
        print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
        print(colors.REDBB+"YOU BUST"+colors.END)
        print(colors.REDBB+"YOU LOST"+colors.END)
        return -1
    #If Plaver gets higher
    elif (playerCount > dealerCount):
        if (len(player)==2 and playerCount==21):
            print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
            print(colors.GREENB+"YOU WON w/ BLACKJACK"+colors.END)            
            return 2
        else:
            print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
            print(colors.GREENB+"YOU WON"+colors.END)
            return 1
    #If Dealer gets higher
    elif (playerCount < dealerCount):
        print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
        print(colors.REDBB+"YOU LOST"+colors.END)
        return -1   
   #If they are equal
    elif (playerCount == checkScore(dealer)):
        #If Player had Blackjack
        if (len(player)==2 and playerCount==21) and len(dealer)>2:
            print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
            print(colors.GREENB+"YOU WON w/ BLACKJACK"+colors.END)            
            return 2
        #If Dealer had Blackjack
        elif (len(player)>2 and playerCount==21) and len(dealer)==2:
            print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
            print(colors.REDBB+"YOU LOST, DEALER HAD BLACKJACK"+colors.END)    
            return -1
        #Else they are just a tie
        else: 
            print(colors.CYANB+"Player: "+colors.END + str(playerCount) + colors.REDB+"\nDealer: "+colors.END + str(dealerCount))
            print("PUSH")
            return 0     
    

#Plays out a Single Round    
def startRound(bet, balance, deck)->int:
    #Give 2 Cards to Dealer
    dealerhand = [deck.pop(),deck.pop()] 
    #Give 2 Cards to Player
    playerhand = [deck.pop(),deck.pop()]

    print(colors.CYANB+"Your Hand:"+colors.END)
    print(colors.CYAN + str(playerhand) + " -> " + str(checkScore(playerhand))+ colors.END)
    print(colors.REDB+"\nDealer's Up Card:"+colors.END)
    
    #Show Dealer's Up Card
    print(colors.RED + "["+dealerhand[0]+"]\n"+ colors.END)
    
   #Inital Options for Player (Includes Double)
    while True:
        userIn = input('What would you like to do?\n-\'H\'it -\'S\'tand -\'D\'ouble   : ')
        if (userIn.upper() == 'H'):
            while (hitCard(playerhand,deck)):
                continue
            break
        elif(userIn.upper() == 'S'):
            break
        elif(userIn.upper() == 'D'):
            if (bet*2 > balance):
                print("You don't have enough money to double")
                continue
            else:
                playerhand.append(deck.pop())
                print(colors.CYANB+"Player Cards"+colors.END)
                print(str(playerhand) + " -> " + str(checkScore(playerhand)))              
                
                bet = bet + bet
                break
        else:
            print(colors.REDBB + "Invalid Input" + colors.END)
            

            
    dealerTurn(dealerhand,deck)  
    
    #Checks the result of the game
    result = (evalRound(playerhand,dealerhand))
    
    #Player Wins
    if result==1: 
        balance += bet
    #Dealer Wins
    elif result==-1:
        balance -= bet
    #Player Wins from Blackjack
    elif result ==2:
        balance += math.ceil(bet * 1.5)
    
    print("New Balance: " + str(balance) + "\n")
    return balance
    
#Plays the game till User runs out of money   
def startGame(balance)->None:
    gameDeck = makeShoe()
    #Game goes until the user runs out of money
    while (balance > 0):
        bet = input('How much would you like to bet?   : ')
        try:
            bet = int(bet)

        except:
            print(colors.REDBB + "Invalid Input" + colors.END)
            continue
        if (bet>balance):
            print("Not enough money!")
        else:
            #Balance gets updated each round
            balance = startRound(bet,balance,gameDeck)        
            
    
if __name__ == '__main__':

    #Takes intial balance
    while True: 
        balance = input('How much would you like to play with today?   : ')

        try: 
            balance = int(balance)
        except:
            print(colors.REDBB + "Invalid Input: balance must be a number " + colors.END)
            continue
            
        startGame(balance)
#has to be run as a script  
print(colors.REDB + "Game Over" + colors.END)