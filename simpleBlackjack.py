def evaluate(hand):
    #function that checks if hand is a flush, checks for each suit in hand, odd-numbered locations 
    def poker_flush(hand):
        suit = hand[1]
        for i in range(1, len(hand), 2):
            if hand[i] != suit:
                return None
        return 'Flush'
                
    #nested loop to check even-numbered char, returns count
    #counter is used to differentiate between the four kind of hand combinations 
    def count_ranks(hand):
        counter = 0
        for i in range(0, len(hand), 2):
            for j in range(i+2, len(hand)):
                if hand[i] == hand[j]:
                    counter += 1
        if counter == 6:
            return 'Four of a kind.'
        if counter == 4:
            return 'Full House.'
        if counter == 3:
            return 'Three of a kind.'
        if counter == 1:
            return 'Pair.'
    #first loop checks if each suit is either AKQJ, written from largest possible suit to lowest in that range
    #it breaks right after since there will not be any other larger
    #if char a number, including 10 as T, stores and return largest char          
    def poker_high(hand):
        High_rank = ''
        for i in range(0, len(hand), 2):        
            if hand[i] in 'AKQJ':
                if hand[i] == 'A':
                    return 'A'
                    break
                if hand[i] == 'K':
                    return 'K'
                    break
                if hand[i] == 'Q':
                    return 'Q'
                    break
                if hand[i] == 'J':
                    return 'J'
                    break
            if hand[i] in '23456789T':
                hand[i] > High_rank
                High_rank = hand[i]
        return High_rank + ' high'
    return poker_flush(hand), count_ranks(hand), poker_high(hand) 
