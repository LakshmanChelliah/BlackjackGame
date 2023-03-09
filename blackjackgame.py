
import random
import math

# Authors: Lakshman Chelliah, Dylan Dominic

SHOE_SIZE = 6
DEALER_HIT_ON = 16

#Creates BlackJack Shoe with SHOE_SIZE amount of decks 
def makeShoe()->list:
    deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    symbols = ["♠","♥","♦","♣"]
    
    finaldeck = [];

    for x in symbols:
        for y in deck:
            finaldeck.append(str(x) + str(y))
    finaldeck = finaldeck*SHOE_SIZE
    random.shuffle(finaldeck)
    
    return finaldeck


#Converts Cards in Hand to a Value to be compared with opponent 
#Looks at Number of "A" and determines when the best value with n Aces
def checkScore(hand) -> int:
    score = 0
    aceCount = 0
    
    for card in hand:
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
            
            
    while score > 21 and aceCount > 0:
        score -= 10
        aceCount -= 1
            
    return score
    
    
#Made for Player
#Gives another card until not needed
def hitCard (hand, deck)->bool:
    hand.append(deck.pop())
    print("Player Cards")
    print(hand)
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
                print("Invalid Input")
                userIn = input('What would you like to do?\n-\'H\'it -\'S\'tand   : ')


#Dealer's Version of hitCard
#Dealer will hit on DEALER_HIT_ON
def dealerTurn(hand, deck)->None:
    
    print("Dealers Cards")
    print(hand)
    
    while (checkScore(hand) < DEALER_HIT_ON):
        print("Dealer HIT")
        hand.append(deck.pop())
        print(hand)
      
        
#Evalutes round and returns:
#1 for Player 
#-1 for Dealer
#0 for Tie
#2 for Blackjack
def evalRound(player, dealer)->int:
    
    playerBust = checkScore(player) > 21
    dealerBust = checkScore(dealer) > 21
    
    print('\n')
    if (dealerBust and not playerBust):
        print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
        print("DEALER BUST")
        print("YOU WON")
        return 1
    elif (playerBust and not dealerBust):
        print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
        print("YOU BUST")
        print("YOU LOST")
        return -1
    elif (playerBust and dealerBust):
        print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
        print("BOTH BUST")
        print("PUSH")
        return 0
    elif (checkScore(player) > checkScore(dealer)):
        if (len(player)==2 and checkScore(player)==21):
            print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
            print("YOU WON w/ BLACKJACK")            
            return 2
        else:
            print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
            print("YOU WON")
            return 1
    elif (checkScore(player) < checkScore(dealer)):
        print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
        print("YOU LOST")
        return -1   
    elif (checkScore(player) == checkScore(dealer)):
        print("Player: " + str(checkScore(player)) + "\nDealer: " + str(checkScore(dealer)))
        print("PUSH")
        return 0     
    

#Plays out a Single Round    
def startRound(bet, balance, deck)->int:
    
    dealerhand = [deck.pop(),deck.pop()] 
    
    playerhand = [deck.pop(),deck.pop()]
    print("Your Hand:")
    print(playerhand)
    print("\nDealer's Up Card:")
    print("["+dealerhand[0]+"]\n")
    
   
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
                print("Player Cards")
                print(playerhand)                
                
                bet = bet + bet
                break
        else:
            print("Invalid Input")
            

            
    dealerTurn(dealerhand,deck)  
    
    result = (evalRound(playerhand,dealerhand))
    
    if result==1: 
        balance += bet
    elif result==-1:
        balance -= bet
    elif result ==2:
        balance += math.ceil(bet * 1.5)
    
    print("New Balance: " + str(balance) + "\n")
    return balance
    
#Plays the game till User runs out of money   
def startGame(balance)->None:
    gameDeck = makeShoe()
    while (balance > 0):
        bet = input('How much would you like to bet?   : ')
        try:
            bet = int(bet)

        except:
            print("Invalid Input")
            continue
        if (bet>balance):
            print("Not enough money!")
        else:
            balance = startRound(bet,balance,gameDeck)        
            
    
if __name__ == '__main__':

    while True: 
        balance = input('How much would you like to play with today?   : ')

        try: 
            balance = int(balance)
            startGame(balance)
            break
        except:
            print("Invalid Input")

print("Game Over")
    
    