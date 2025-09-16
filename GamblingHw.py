#Brainstorm 04/09/25
#Nvm its our whole project are we cooked gng
"""
Hi, welcome to our casino! There's a lot to explain so just follow any comments you see ig otherwise you |CANNOT| read it :(
All of these a1 / b5 / d14 are a variable for a potential player (Its why 15 max yk) and they have a value thats their cash
limit. this cash limit will be deducted at casinos. the letter at start and number at end relate to personality, 0 is normal,
4 is shy guy, ect. i did not use 2 because i forgot the number 2 existed (fun story) so ignore that. cya!
"""
import random
a1 = 1000000
a2 = 1000000
a3 = 1000000
a4 = 1000000
a5 = 1000000
a6 = 1000000
a7 = 1000000
a8 = 1000000
a9 = 1000000
a10 = 1000000
a11 = 1000000
a12 = 1000000
a13 = 1000000
a14 = 1000000
a15 = 1000000
FullList = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15] #List of all normal personalities to be used later
b1 = 1000001
b2 = 1000001
b3 = 1000001
b4 = 1000001
b5 = 1000001
b6 = 1000001
b7 = 1000001
b8 = 1000001
b9 = 1000001
b10 = 1000001
b11 = 1000001
b12 = 1000001
b13 = 1000001
b14 = 1000001
b15 = 1000001
RandList = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15] #Same but random
c1 = 1000003
c2 = 1000003
c3 = 1000003
c4 = 1000003
c5 = 1000003
c6 = 1000003
c7 = 1000003
c8 = 1000003
c9 = 1000003
c10 = 1000003
c11 = 1000003
c12 = 1000003
c13 = 1000003
c14 = 1000003
c15 = 1000003
AllInList = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15] #same but all in
d1 = 1000004
d2 = 1000004
d3 = 1000004
d4 = 1000004
d5 = 1000004
d6 = 1000004
d7 = 1000004
d8 = 1000004
d9 = 1000004
d10 = 1000004
d11 = 1000004
d12 = 1000004
d13 = 1000004
d14 = 1000004
d15 = 1000004
ShyList = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15] #same but small spender, codename shy guy
PlayerList = [] #what balances to keep track of
Players = int(input("Enter your total amount of players:")) #Now we select players, games and traits. should be readable
while Players > 15:
    print("Too many, max is 15")
    Players = int(input("Enter your total amount of players:"))
TotalGames = int(input("Enter your total amount of simulated games:"))
while TotalGames > 250:
    print("Too many, max is 250")#
    TotalGames = int(input("Enter your total amount of simulated games:"))
Trait = input("Do you want traits? (Yes / No)")
if Trait == "No":
    for y in range (0, Players):
        PlayerList.append(FullList[y]) #this just adds them and then starts us gambling!!!
elif Trait == "Yes":
    Normal = int(input("Enter your total amount of normal players:"))
    while Normal > Players: #Makes sure we dont go over cap of 15 cause a1-a15 all we got !!!
        print("Too many, max is 15")
        Normal = int(input("Enter your total amount of normal players:"))
    for y in range (0, Normal):
        PlayerList.append(FullList[y])
    Random = int(input("Enter your total amount of random players:"))
    while Normal + Random > Players:
        print("Too many, max is 15")
        Random = int(input("Enter your total amount of random players:"))
    for y in range (0, Random):
        PlayerList.append(RandList[y]) #Àppends specifically random, its why we needed those multiple lists!
    AllIn = int(input("Enter your total amount of all in players:"))
    while Normal + Random + AllIn > Players:
        print("Too many, max is 15")
        AllIn = int(input("Enter your total amount of all in players:"))
    for y in range (0, AllIn):
        PlayerList.append(AllInList[y])
    Shy = int(input("Enter your total amount of small spender players:"))
    while Normal + Random + AllIn + Shy > Players:
        print("Too many, max is 15")
        Shy = int(input("Enter your total amount of small spender players:"))
    for y in range (0, Shy):
        PlayerList.append(ShyList[y]) #Up to here is just assigning traits, already 110 lines in is NOT a good sign but anyways...
        
#Now we define ALL of our games

def SlotGame(P0): #This was created by jakub / melon. i slightly tweaked it but his code was commented himself (Very neatly)
    symbols = ["🍒"]*6 + ["🍋"]*6 + ["🔔"]*6 + ["⭐"]*3 + ["7"]*1
    def spin_reels():
        """Return 3 random symbols based on weighted probabilities."""
        return [random.choice(symbols) for _ in range(3)]

    def check_win(reels, bet):
        """
        Check if the player won based on reels outcome.
        - 3 match: bigger prize (rare)
        - Anthony added feature: if 3 of a kind for rarer, gives us a LOT of bet back (we still profit however)
        - 2 match: small prize
        - Otherwise: lose
        """
        if reels.count(reels[0]) == 3:       # All 3 match
            if reels.count("🍒") == 3 or reels.count("🍋") == 3 or reels.count("🔔") == 3:
                return bet * 3   # Lowered multiplier
            elif reels.count("⭐") == 3:
                return bet * 5
            elif reels.count("7") == 3:
                return bet * 10
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:  #2 match
            return bet // 2  # Only half the bet back
        else:
            return 0
        
    balance = P0 #sets money
    Strbalance = str(balance) #string to see what type of gambler
    if (Strbalance[-1]) == "0": #if normal player detected
        bet = 40 #puts bet
    elif (Strbalance[-1]) == "1":
        bet = ((random.randint(1,5)) * 20)
    elif (Strbalance[-1]) == "3":
        bet = 100
    elif (Strbalance[-1]) == "4":
        bet = 20
    play = TotalGames #how many times
    spins = int(play) #turns into int to make playable, here cause i changed code (Anthony)

    for _ in range(spins):
        
        balance -= bet  # subtract bet for each spin
        reels = spin_reels()
        #print(" | ".join(reels))
        
        winnings = check_win(reels, bet)
        if winnings > 0:
            #print(f"You won €{winnings}!") # isnerts a string where the squigly line is( very useful for this type stuff )
            balance += winnings
    return balance

def GamblingPoker(P1_t, P2_t, P3_t, P4_t): #P1_t is our player 1 total, just wanted to clear. This is how poker is played (Slots alr done)
    Pot = 0 #Total winnings
    P1 = [] #For player cards
    P2 = []
    P3 = []
    P4 = []
    HangingNum = [] 
    CardsMain=["HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
              "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
              "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",
              "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK"] #All of our cards
    Cards=["HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK",
           "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK",
           "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK",
           "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK"] #Again to be replaced

    WinningList = [] #What the chosen cards are

    def WinCalc(P0): #This calculates our winner at the end
        HandValue = 0 #how good hand was
        Club = P0.count("C")  #sees if flush
        Spade = P0.count("S")
        Heart = P0.count("H")
        Diamond = P0.count("D")
        if Club == 5:#if flush you get good score to win
            HandValue = 4
            return HandValue
        elif Spade == 5:
            HandValue = 4
            return HandValue
        elif Heart == 5:
            HandValue = 4
            return HandValue
        elif Diamond == 5:
            HandValue = 4
            return HandValue
        for y in range(2, 11): #this sees if you had a pair or 3 of a kind, ect
            Count = P0.count(str(y)) #counts as proof of above
            if Count == 2:
                HandValue = 2
                return HandValue
            elif Count == 3:
                HandValue = 3
                return HandValue
            elif Count == 4:
                 HandValue = 5
                 return HandValue
            elif Count > 0:
                 HandValue = (y/10) #or makes it so our highcard is value
        Ace = P0.count("A")
        King = P0.count("K")
        Queen = P0.count("Q")
        Jack = P0.count("J")
        if Ace > 0:
            HandValue = 1.75
            return HandValue
        elif King > 0:
            HandValue = 1.5
            return HandValue
        elif Queen > 0:
            HandValue = 1.25
            return HandValue
        elif Jack > 0:
            HandValue = 1.1
            return HandValue
        else:
            return HandValue #double checks on J/Q/K/A same
    def GamblingRound1(P0, Num): # I want player to decide to gamble if cards are good enough, round 2-4 are same so only comment this!!!
        GoIn = 0
        Value = 0
        Club = P0.count("C")#counts all our suits
        Spade = P0.count("S")
        Heart = P0.count("H")
        Diamond = P0.count("D")
        if Club == 2:#If close to a flush, bet!
            GoIn += 1
        elif Spade == 2:
            GoIn += 1
        elif Heart == 2:
            GoIn += 1
        elif Diamond == 2:
            GoIn += 1 #If same suit they SHOULD bet
        for y in range(2, 11):
            Count = P0.count(str(y))
            Value += (Count*y) #Count value of cards, if 15 or higher we go bet
            if Count == 2: #ALSO if pair or higher, bet!!!
                GoIn += 5
        Count = P0.count("J")
        Value += (Count*10)
        if Count == 2:
            GoIn += 5 #Same thing but face cards
        Count = P0.count("Q")
        Value += (Count*10)
        if Count == 2:
            GoIn += 6
        Count = P0.count("K")
        Value += (Count*15)
        if Count == 2:
            GoIn += 7
        Count = P0.count("A")
        Value += (Count*20)
        if Count == 2:
            GoIn += 10
        StrP0 = str(P0) #This is our player turned into string to see what gamble type
        if StrP0[-1] == "0": #it checks last digit to compare identifier earlier (i couldnt think of other solution and it worked easy
            if Value > 14:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 0:
               # print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,2) == 1: # to sum up, if you got good cards it decides to bet, depends on personality trait. thats it!!!
                #print("Player", Num, "is betting with:", P0)
                return Num #it decided if cards are good based on "Value" we assigned before, or takes a random chance and bluffs
        elif StrP0[-1] == "1":
            if random.randint(1,5) != 5:
                return Num
        elif StrP0[-1] == "3":
            return Num
        elif StrP0[-1] == "4":
            if Value > 19:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 0:
               # print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,3) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num #Same for other personalities but tailored to them!!! basic commenting will be left for rest of these as theyre same

    def GamblingRound2(P0, Num): # I want player to decide to gamble if cards are good enough
        GoIn = 0
        Value = 0
        Club = P0.count("C")
        Spade = P0.count("S")
        Heart = P0.count("H")
        Diamond = P0.count("D")
        if Club > 2:
            GoIn += 2
        elif Spade > 2:
            GoIn += 2
        elif Heart > 2:
            GoIn += 2
        elif Diamond > 2:
            GoIn += 2 #If same suit they SHOULD bet
        for y in range(2, 11):
            Count = P0.count(str(y))
            Value += (Count*y) #Count value of cards, if 15 or higher we go bet
            if Count == 2:
                GoIn += 5
            elif Count > 2:
                GoIn += 15
        Count = P0.count("J")
        Value += (Count*10)
        if Count == 2:
            GoIn += 5 #Same thing but face cards
        elif Count > 2:
                GoIn += 30
        Count = P0.count("Q")
        Value += (Count*10)
        if Count == 2:
            GoIn += 6
        elif Count > 2:
            GoIn += 30
        Count = P0.count("K")
        Value += (Count*15)
        if Count == 2:
            GoIn += 7
        elif Count > 2:
            GoIn += 35
        Count = P0.count("A")
        Value += (Count*20)
        if Count == 2:
            GoIn += 10
        elif Count > 2:
            GoIn += 50
        StrP0 = str(P0)
        if StrP0[-1] == "0":
            if Value > 20:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,3) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
        elif StrP0[-1] == "1":
            if random.randint(1,4) != 4:
                return Num
        elif StrP0[-1] == "3":
            return Num
        elif StrP0[-1] == "4":
            if Value > 25:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,4) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num

    def GamblingRound3(P0, Num): # I want player to decide to gamble if cards are good enough
        GoIn = 0
        Value = 0
        Club = P0.count("C")
        Spade = P0.count("S")
        Heart = P0.count("H")
        Diamond = P0.count("D")
        if Club > 2:
            GoIn += 2
        elif Spade > 2:
            GoIn += 2
        elif Heart > 2:
            GoIn += 2
        elif Diamond > 2:
            GoIn += 2 #If same suit they SHOULD bet
        for y in range(2, 11):
            Count = P0.count(str(y))
            Value += (Count*y) #Count value of cards, if 15 or higher we go bet
            if Count == 2:
                GoIn += 1
            elif Count > 2:
                GoIn += 15
        Count = P0.count("J")
        Value += (Count*10)
        if Count == 2:
            GoIn += 5 #Same thing but face cards
        elif Count > 2:
                GoIn += 30
        Count = P0.count("Q")
        Value += (Count*10)
        if Count == 2:
            GoIn += 6
        elif Count > 2:
            GoIn += 30
        Count = P0.count("K")
        Value += (Count*15)
        if Count == 2:
            GoIn += 7
        elif Count > 2:
            GoIn += 35
        Count = P0.count("A")
        Value += (Count*20)
        if Count == 2:
            GoIn += 10
        elif Count > 2:
            GoIn += 50
        StrP0 = str(P0)
        if StrP0[-1] == "0":
            if Value > 18:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,4) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
        elif StrP0[-1] == "1":
            if random.randint(1,4) != 4:
                return Num
        elif StrP0[-1] == "3":
            return Num
        elif StrP0[-1] == "4":
            if Value > 25:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,4) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num

    def GamblingRound4(P0, Num): # I want player to decide to gamble if cards are good enough
        GoIn = 0
        Value = 0
        Club = P0.count("C")
        Spade = P0.count("S")
        Heart = P0.count("H")
        Diamond = P0.count("D")
        if Club > 3:
            GoIn += 2
        elif Club == 2:
            GoIn += 1
        elif Spade > 3:
            GoIn += 2
        elif Spade == 2:
            GoIn += 1
        elif Heart > 3:
            GoIn += 2
        elif Heart == 2:
            GoIn += 1
        elif Diamond > 3:
            GoIn += 2
        elif Diamond == 2:
            GoIn += 1#If same suit they SHOULD bet
        for y in range(2, 11):
            Count = P0.count(str(y))
            Value += (Count*y) #Count value of cards, if 15 or higher we go bet
            if Count == 2:
                GoIn += 1
            elif Count > 2:
                GoIn += 15
        Count = P0.count("J")
        Value += (Count*10)
        if Count == 2:
            GoIn += 5 #Same thing but face cards
        elif Count > 2:
                GoIn += 30
        Count = P0.count("Q")
        Value += (Count*10)
        if Count == 2:
            GoIn += 6
        elif Count > 2:
            GoIn += 30
        Count = P0.count("K")
        Value += (Count*15)
        if Count == 2:
            GoIn += 7
        elif Count > 2:
            GoIn += 35
        Count = P0.count("A")
        Value += (Count*20)
        if Count == 2:
            GoIn += 10
        elif Count > 2:
            GoIn += 50
        StrP0 = str(P0)
        if StrP0[-1] == "0":
            if Value > 22:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,4) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num
        elif StrP0[-1] == "1":
            if random.randint(1,4) != 4:
                return Num
        elif StrP0[-1] == "3":
            return Num
        elif StrP0[-1] == "4":
            if Value > 25:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif GoIn > 2:
                #print("Player", Num, "is betting with:", P0)
                return Num
            elif random.randint(1,5) == 1:
                #print("Player", Num, "is betting with:", P0)
                return Num

    for y in range(0, 8): #NOW we start the game, that was defining functions
        CurrentCard = random.randint(0, (len(Cards)-1))#'This deals out random cards. could it have been neater? maybe if i could code better
        CurrentCard = Cards[CurrentCard]#picks a random card from card list, adds it to a new list so we can have players take
        HangingNum.append(CurrentCard) #calls 8 for the 4 players and no repeats
        Cards.remove(CurrentCard) #removes from deck!
    P1.append(HangingNum[0]) #gives them out
    P1.append(HangingNum[1])
    P2.append(HangingNum[2])
    P2.append(HangingNum[3])
    P3.append(HangingNum[4])
    P3.append(HangingNum[5])
    P4.append(HangingNum[6])
    P4.append(HangingNum[7])
    P1Str = str(P1)#once again to analyze cards we make into strings, lists have special rules that strings do not!
    P2Str = str(P2)
    P3Str = str(P3)
    P4Str = str(P4)

    HangingNum.clear()

    # Now lets go do the game ;D

    """BREAK TO SHOW THAT ACTUAL GAME IS BELOW!!!
    --------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------
    This is for my sanity """
    while True:
        #print("Round 1:\n")
        WinningList.append(GamblingRound1(P1Str, 1))#does our function and sees if they go or not
        WinningList.append(GamblingRound1(P2Str, 2))
        WinningList.append(GamblingRound1(P3Str, 3))
        WinningList.append(GamblingRound1(P4Str, 4))
        
        for y in range (0, 4):#this removes all players who folded (Fold depends on if they reterned (num) which was their number of player
            if WinningList.count(None) > 0:
                WinningList.remove(None)
        if len(WinningList) == 1: #if only one person betted:
            #print()
           # print("Player", WinningList, "won!")
            Winner = WinningList[0] #they win and are paid!
            if Winner == 1:
                Pot = ((Pot // 10) * 9) #not the whole pot, dealer and casino get a "cut" if you know what i mean
                P1_t += Pot
            if Winner == 2:
                Pot = ((Pot // 10) * 9)
                P2_t += Pot #checks every player cause it could be 1-4 and these are so small i didnt feel the need to add MORE functions.
            if Winner == 3:
                Pot = ((Pot // 10) * 9)
                P3_t += Pot
            if Winner == 4:
                Pot = ((Pot // 10) * 9)
                P4_t += Pot
            break
        elif len(WinningList) == 0: #if no one won house takes all
            #print()
            #print("The house wins!")
            Pot = 0
            break

        for y in range(0, 3): #picks up 3 more cards same way as before for next round
            CurrentCard = random.randint(0, (len(Cards)-1))
            CurrentCard = Cards[CurrentCard]
            HangingNum.append(CurrentCard)
            Cards.remove(CurrentCard)

        if WinningList.count(1) == 1: #if we didnt fold (Checked by bum) we get new cards !!! 
            P1.append(str(HangingNum))
            P1_t -= 10
            Pot += 10 #also we bet more and add to the pot
        if WinningList.count(2) == 1:
            P2.append(str(HangingNum))
            P2_t -= 10
            Pot += 10
        if WinningList.count(3) == 1:
            P3.append(str(HangingNum))
            P3_t -= 10
            Pot += 10
        if WinningList.count(4) == 1:
            P4.append(str(HangingNum))
            P4_t -= 10
            Pot += 10

        """ROUND TWO CODE
        --------------------------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------------
        SPACE"""



        #print("\nRound 2:\nTable's Flop:", HangingNum, "\n")
        
        P1Str = str(P1) #This code repeatts near exacrlt til round 4 so i will comment there again
        P2Str = str(P2)
        P3Str = str(P3)
        P4Str = str(P4)

        if WinningList.count(1) == 1:
            WinningList.remove(1)
            WinningList.append(GamblingRound2(P1Str, 1))
        if WinningList.count(2) == 1:
            WinningList.remove(2)
            WinningList.append(GamblingRound2(P2Str, 2))
        if WinningList.count(3) == 1:
            WinningList.remove(3)
            WinningList.append(GamblingRound2(P3Str, 3))
        if WinningList.count(4) == 1:
            WinningList.remove(4)
            WinningList.append(GamblingRound2(P4Str, 4))
            
        for y in range (0, 4):
            if WinningList.count(None) > 0:
                WinningList.remove(None)
        if len(WinningList) == 1:
            #print()
            #print("Player", WinningList, "won!")
            Winner = WinningList[0]
            if Winner == 1:
                Pot = ((Pot // 10) * 9)
                P1_t += Pot
            if Winner == 2:
                Pot = ((Pot // 10) * 9)
                P2_t += Pot
            if Winner == 3:
                Pot = ((Pot // 10) * 9)
                P3_t += Pot
            if Winner == 4:
                Pot = ((Pot // 10) * 9)
                P4_t += Pot
            break
        elif len(WinningList) == 0:
            #print()
            #print("The house wins!")
            Pot = 0
            break


        HangingNum1 = list(HangingNum)
        HangingNum.clear()
        CurrentCard = random.randint(0, (len(Cards)-1))
        CurrentCard = Cards[CurrentCard]
        HangingNum.append(CurrentCard)
        Cards.remove(CurrentCard)
        HangingNum1 = HangingNum1 + HangingNum

        if WinningList.count(1) == 1:
            P1.append(str(HangingNum))
            P1_t -= 30
            Pot += 30
        if WinningList.count(2) == 1:
            P2.append(str(HangingNum))
            P2_t -= 30
            Pot += 30
        if WinningList.count(3) == 1:
            P3.append(str(HangingNum))
            P3_t -= 30
            Pot += 30
        if WinningList.count(4) == 1:
            P4.append(str(HangingNum))
            P4_t -= 30
            Pot += 30


        """ THIRD ROUND SO CLOSE !!!
        --------------------------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------------
        YIPPEE!!!"""

        #print("\nRound 3:\nTable's Flip:", HangingNum1, "\n")

        P1Str = str(P1)
        P2Str = str(P2)
        P3Str = str(P3)
        P4Str = str(P4)

        if WinningList.count(1) == 1:
            WinningList.remove(1)
            WinningList.append(GamblingRound3(P1Str, 1))
        if WinningList.count(2) == 1:
            WinningList.remove(2)
            WinningList.append(GamblingRound3(P2Str, 2))
        if WinningList.count(3) == 1:
            WinningList.remove(3)
            WinningList.append(GamblingRound3(P3Str, 3))
        if WinningList.count(4) == 1:
            WinningList.remove(4)
            WinningList.append(GamblingRound3(P4Str, 4))
        
        for y in range (0, 4):
            if WinningList.count(None) > 0:
                WinningList.remove(None)
        if len(WinningList) == 1:
            #print()
            #print("Player", WinningList, "won!")
            Winner = WinningList[0]
            if Winner == 1:
                Pot = ((Pot // 10) * 9)
                P1_t += Pot
            if Winner == 2:
                Pot = ((Pot // 10) * 9)
                P2_t += Pot
            if Winner == 3:
                Pot = ((Pot // 10) * 9)
                P3_t += Pot
            if Winner == 4:
                Pot = ((Pot // 10) * 9)
                P4_t += Pot
            break
        elif len(WinningList) == 0:
            print()
            #print("The house wins!")
            Pot = 0
            break


        HangingNum2 = list(HangingNum1)
        HangingNum.clear()
        CurrentCard = random.randint(0, (len(Cards)-1))
        CurrentCard = Cards[CurrentCard]
        HangingNum.append(CurrentCard)
        Cards.remove(CurrentCard)
        HangingNum2 = HangingNum2 + HangingNum

        if WinningList.count(1) == 1:
            P1.append(str(HangingNum))
            P1_t -= 50
            Pot += 50
        if WinningList.count(2) == 1:
            P2.append(str(HangingNum))
            P2_t -= 50
            Pot += 50
        if WinningList.count(3) == 1:
            P3.append(str(HangingNum))
            P3_t -= 50
            Pot += 50
        if WinningList.count(4) == 1:
            P4.append(str(HangingNum))
            P4_t -= 50
            Pot += 50

        """FINAL ROUND !!!
        --------------------------------------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------------
        YIPPEE!!!"""

        #print("\nRound 4:\nTable's River:", HangingNum2, "\n")

        P1Str = str(P1)
        P2Str = str(P2)
        P3Str = str(P3)
        P4Str = str(P4)

        if WinningList.count(1) == 1:
            WinningList.remove(1)
            WinningList.append(GamblingRound4(P1Str, 1))
        if WinningList.count(2) == 1:
            WinningList.remove(2)
            WinningList.append(GamblingRound4(P2Str, 2))
        if WinningList.count(3) == 1:
            WinningList.remove(3)
            WinningList.append(GamblingRound4(P3Str, 3))
        if WinningList.count(4) == 1:
            WinningList.remove(4)
            WinningList.append(GamblingRound4(P4Str, 4))
        
        for y in range (0, 4):
            if WinningList.count(None) > 0:
                WinningList.remove(None)

        """
        Now its the hard part oh no...#
        we gotta compare winners (nil)
        wish me luck cause its 5pm on a sunday and i got so much other hw !!!
        """


        if len(WinningList) > 1: #Now is the winning selection... if there is more than 1 winner we do our compare function
            HighestValue = 0
            if WinningList.count(1) == 1: #firstly checks if it has betted to see if it can win.
                P1 = WinCalc(P1Str) #calculates how good cards were
                if P1 > HighestValue: #if they are the highest, store it!
                    HighestValue = int(P1)
            if WinningList.count(2) == 1: #same for every player
                P2 = WinCalc(P2Str)
                if P2 > HighestValue:
                    HighestValue = int(P2)
            if WinningList.count(3) == 1:
                P3 = WinCalc(P3Str)
                if P3 > HighestValue:
                    HighestValue = int(P3)
            if WinningList.count(4) == 1:
                P4 = WinCalc(P4Str)
                if P4 > HighestValue:
                    HighestValue = int(P4)
            if P1 == HighestValue: #if player was highest value they win!
                P1_t+= Pot
            elif P2 == HighestValue: #repeats for each
                P2_t+= Pot
            elif P3 == HighestValue:
                P3_t+= Pot
            elif P4 == HighestValue:
                P4_t+= Pot
            break

        if len(WinningList) == 1: #same as before for 1 winner
            #print()
            #print("Player", WinningList, "won!")
            Winner = WinningList[0]
            if Winner == 1:
                Pot = ((Pot // 10) * 9)
                P1_t += Pot
            if Winner == 2:
                Pot = ((Pot // 10) * 9)
                P2_t += Pot
            if Winner == 3:
                Pot = ((Pot // 10) * 9)
                P3_t += Pot
            if Winner == 4:
                Pot = ((Pot // 10) * 9)
                P4_t += Pot
            break
        elif len(WinningList) == 0:
            #print()
            #print("The house wins!")
            Pot = 0
            break   

        if WinningList.count(1) == 1: #gives a final "tip" to the casino
            P1.append(str(HangingNum))
            P1_t -= 100
            Pot += 100
        if WinningList.count(2) == 1:
            P2.append(str(HangingNum))
            P2_t -= 100
            Pot += 100
        if WinningList.count(3) == 1:
            P3.append(str(HangingNum))
            P3_t -= 100
            Pot += 100
        if WinningList.count(4) == 1:
            P4.append(str(HangingNum))
            P4_t -= 100
            Pot += 100
        break
    EndingList = [] #this is to return values so they dont freak out, puts them in a list and sends them through so they can be seperated while 
    EndingList.append(P1_t) #arriving as one
    EndingList.append(P2_t)
    EndingList.append(P3_t)
    EndingList.append(P4_t)
    return EndingList #returns ending cash

"""
I DID IT OMG NOW GAMING TIME FOR MELON AND JACK'S CODE
Jack never sent on code :(
I'll do melons for now, 21:51 16/09/25
"""

for y in range (0, TotalGames): #for every game that is asked to run
    Backup = [] #backup list so we record whos wallet and balance is whos
    PlayerPick = random.randint(0, (Players-1))
    P1 = PlayerList[PlayerPick]
    Backup.append(PlayerPick)
    PlayerPick = random.randint(0, (Players-1))
    P2 = PlayerList[PlayerPick]
    Backup.append(PlayerPick)
    PlayerPick = random.randint(0, (Players-1)) #selects a random player
    P3 = PlayerList[PlayerPick] #adds them
    Backup.append(PlayerPick) #adds to backup to track
    PlayerPick = random.randint(0, (Players-1))
    P4 = PlayerList[PlayerPick]
    Backup.append(PlayerPick) 

    EndingListMain = GamblingPoker(P1, P2, P3, P4) #adds to main list of values
    First = Backup[0] #EVERYTHING breaks if i dont use these, please leave in :pray:
    Second = Backup[1] #code doesnt like when i call list1[list2[3]]
    Third = Backup[2] #so i do in 2 seperate steps
    Fourth = Backup[3]
    PlayerList[First] = EndingListMain[0] #correlates money to player AFTER poker yay
    PlayerList[Second] = EndingListMain[1] #same for each player
    PlayerList[Third] = EndingListMain[2]
    PlayerList[Fourth] = EndingListMain[3]
    
    #melon gamble game time
    
    PlayerPick = random.randint(0, (Players-1)) #picks random player
    P1 = PlayerList[PlayerPick] #gives them a name
    
    WinNum = SlotGame(P1) #money they win / lose is related to game ofc
    PlayerList[PlayerPick] = WinNum #updates wallet / balance

CurrentPlayers = 0 #sees how many players we had from each type
for y in range(0, (Players-1)):
    CurrentPlayers += PlayerList[y] #adds up their total winnings!
CasinoProfit = (len(PlayerList)*10000000) - CurrentPlayers #calculates how much we made
print()
print("Total Casino Profit ||", CasinoProfit) #prints it (hope you enjoyed i tried to make this readable! enjoy marking i guess)