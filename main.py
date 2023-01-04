import random
from art import logo


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []

ai_card = []

#deals the cards
def deal_cards(cards):
    card = random.choice(cards)
    return card

#checks if score is 21 with only 2 cards, or checks if score is over 21 and it will change the 11 to a 1
def calculated_score(cards):
    if sum(cards) == 21 and len(player_card) == 2:
        return 1
    elif sum(cards) > 21:
        for num in cards:
            if num == 11:
                cards.remove(11)
                cards.append(1)
                cards.sort()
        return sum(cards)
    else:
        return sum(cards)



game = True
while game:
    in_game = True
    while in_game:

        #First two draws for the player and AI.
        for draw in range(2):
            player_card.append(deal_cards(cards))
            ai_card.append(deal_cards(cards))
        if calculated_score(player_card) == 1:
            print("You got a blackjack")
            break
        elif calculated_score(ai_card) == 1:
            print("AI got a blackjack")
            break
        
        total = calculated_score(player_card)
        ai_total = calculated_score(ai_card)
        print(f"Your cards are {player_card}. Your total is: {total}.\n")
        print(f"The AI's first card is {ai_card[0]}.")
        

        #Draws cards for player and AI
        drawing = True
        while drawing:
            deal = input("\nPull card?").lower()
            if deal == "yes":
                player_card.append(deal_cards(cards))
                total = calculated_score(player_card)
                if total > 21:
                    print(f"You Lose! Your total is {total}, ai's total is {ai_total}.")
                    in_game = False
                    break
                print(f"Your cards are {player_card}")
                print(f"Your total is {total}.")

            while ai_total < 17:
                first_draw = random.choice(cards)
                card = first_draw
                ai_card.append(card)
                ai_total = calculated_score(ai_card)

            #checks score between player and AI and decides the winner
            if ai_total > 21:
                print(f"You Win! Your total is {total}, ai's total is {ai_total}.")
                in_game = False
                break
            if deal == "no":
                drawing = False
                in_game = False
                if total == ai_total:
                    print(f"Draw! Your total is {total}, ai's total is {ai_total}. ")
                    
                elif total < ai_total < 21:
                    print(
                        f"You Lose! Your total is {total}, ai's total is {ai_total}.")
                elif 21 > total > ai_total:
                    print(f"You Win! Your total is {total}, ai's total is {ai_total}.")

    #Asks you if you want to play again        
    restart = True
    while restart:
        end = input("Play again type yes, else type no.\n").lower()
        if end == "yes":
            player_card.clear()
            ai_card.clear()
            restart = False
        elif end == "no":
            restart = False
            game = False
        elif end != "yes" and end != "no":
            print("Error! Try Again!")