import random
import tkinter
from tkinter import *
from tkinter import ttk

handSize = 8
playing = True
obtainedConsumable = False
maxShopActions = 5
maxShopRolls = 3
weightSkipBlind = 10
weightRerollBoss = 10
weightBuyUse = 50
weightBuyTwoFromPack = 50
weightSellJoker = 4
weightUseSellConsumable = 40
weightSellConsumable = 20
weightDiscard = 35
maxJokerSlots = 5
maxConsumableSlots = 2
maxShopSlots = 2

def main():
    global playing
    print("Welcome to JokeRNG, the program that tells you how to play Balatro")
    while(playing):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        resp = input("Type 'rules' for an explaination, 'play' to start a game, or 'exit' to quit the program\n").lower()
        if resp == "rules":
            rules()
        elif resp == "play":
            StartGame()
        elif resp == "exit":
            playing = False
            exit()

def InitDeckDefaults():
    global handSize; handSize = 8
    global obtainedConsumable; obtainedConsumable = False
    global maxJokerSlots; maxJokerSlots = 5
    global maxConsumableSlots; maxConsumableSlots = 2


    # Select a deck

    # Go to blind

    # Random sort Rank/Suit
    # Get number of cards held in hand
    # Random select 1 thru 5(or max in hand) cards
    # Random select play/discard
    # Random chance to use/sell consumable

    # Search user input for win/lose

    # Enter shop

    # Random select buy 1/2(/3/4) card in shop, reroll, buy voucher, buy 1/2 pack, use/sell consumable, sell joker, go next
        # maybe chose anywhere from 0-4 options in random order then go next? and things done in order
        # when buying pack, randomize list 1-5 then instruct player to buy in that order from left to right, skipping numbers that don't exist
        # when buying pack or using consumable, randomize list 1-8 and instruct player to select cards in that order until required # of cards is selected. For multiple consumables, continue down list where left off. Restart from beginning of list if necessary.

    # Enter blind select, randon select skip/play

def StartGame():
    InitDeckDefaults()
    global handSize
    global obtainedConsumable
    global maxJokerSlots
    global maxConsumableSlots
    global maxShopSlots
    randomDeck = random.randint(0, 14)
    if(randomDeck == 0):
        print("Select the Red Deck")
    elif(randomDeck == 1):
        print("Select the Blue Deck")
    elif(randomDeck == 2):
        print("Select the Yellow Deck")
    elif(randomDeck == 3):
        print("Select the Green Deck")
    elif(randomDeck == 4):
        print("Select the Black Deck")
        maxJokerSlots = 6
    elif(randomDeck == 5):
        print("Select the Magic Deck")
        obtainedConsumable = True
        maxConsumableSlots = 3
    elif(randomDeck == 6):
        print("Select the Nebula Deck")
        maxConsumableSlots = 1
    elif(randomDeck == 7):
        print("Select the Ghost Deck")
        obtainedConsumable = True
    elif(randomDeck == 8):
        print("Select the Abandoned Deck")
    elif(randomDeck == 9):
        print("Select the Checkered Deck")
    elif(randomDeck == 10):
        print("Select the Zodiac Deck")
        maxShopSlots = 3
    elif(randomDeck == 11):
        print("Select the Painted Deck")
        handSize = 10
        maxJokerSlots = 4
    elif(randomDeck == 12):
        print("Select the Anaglyph Deck")
    elif(randomDeck == 13):
        print("Select the Plasma Deck")
    elif(randomDeck == 14):
        print("Select the Erratic Deck")
    resp = input("\nPress enter to begin play\n")
    PlayBlind()

def PlayBlind():
    print("\n~~~~~~~~~~~~~~~~~~~\n")
    sort = ""
    play = ""

    if(random.randint(0,1) == 0): # Flip whether to sort cards by Rank or by Suit
        sort = "Rank"
    else:
        sort = "Suit"

    if(random.randint(0,1) == 0): # Flip whether to Discard Hand or Play Hand
        play = "Discard"
    else:
        play = "Play"
    pass


    numCards = random.randint(1, 5) # Pick number of cards to select
    cardsInHand = list(range(1, handSize + 1)) # get list of possible number of cards held in hand, then shuffle them
    random.shuffle(cardsInHand)

    if random.randint(1, 100) <= weightSellJoker: # randomly check if we sell a Joker before playing hand
        numJoker = random.randint(1, maxJokerSlots)
        input(f"ACTION: Sell the Joker in slot #{numJoker}, then press enter to continue\n")

    if random.randint(1, 100) <= weightUseSellConsumable and obtainedConsumable: # randomly check if we try to use or sell a Consumable before playing hand
        numCons = random.randint(1, maxConsumableSlots)
        if(random.randint(1, 100) < weightSellConsumable): 
            input(f"ACTION: Sell the consumable in slot #{numCons}, then press enter to continue\n")
        else:
            input(f"ACTION: Use the consumable in slot #{numCons}, then press enter to continue\nIf Necessary, use the following list of cards to select:\n{cardsInHand}\n")
            random.shuffle(cardsInHand)

    resp = input(f"ACTION: Sort Cards by: {sort}. Select {numCards} in order from the following list: {cardsInHand}. {play} these CardsIf you Won or Lost this blind, type win or lose, then press enter to continue\n").lower()
    if resp == "win":
        Win()
    elif resp == "lose":
        Lose()
    else:
        PlayBlind()

def Win():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nBlind has been successfully defeated, entering shop...\n")
    EnterShop()

def Lose():
    input("You're such a Joke\nPress enter to return to start\n\n")

def EnterShop():
    global maxShopActions
    global maxShopRolls
    global maxShopSlots
    global weightBuyUse
    global weightSellJoker
    global maxJokerSlots
    global obtainedConsumable
    global weightBuyTwoFromPack
    showList = False
    voucherPurchased = False
    currentShopRolls = 0
    action = "if you see this something is fukked"
    thisShopActions = random.randint(0, maxShopActions)
    while(thisShopActions > 0):
        showList = False
        cardsInHand = list(range(1, handSize + 1)) # get list of possible number of cards held in hand, then shuffle them
        random.shuffle(cardsInHand)
        thisShopActions -= 1
        shopAction = random.randint(0, 5)
        if(shopAction == 0): # Purchase a card from the shop
            slot = random.randint(1, maxShopSlots)
            BuyUse = random.randint(1, 100)
            obtainedConsumable = True
            if BuyUse > weightBuyUse:
                action = f"ACTION: Buy (Joker/Playing Card) OR Buy+Use (Consumable) the Card in Shop Slot #{slot}"
            else:
                action = f"ACTION: Buy the Card in Shop Slot #{slot}"
        elif(shopAction == 1 and currentShopRolls < maxShopRolls): # Reroll the shop
            currentShopRolls += 1
            action = "ACTION: Reroll the shop one time"            
        elif(shopAction == 2): # Purchase a Voucher
            if(voucherPurchased):
                continue
            action = "ACTION: Purchase the Voucher in the shop"
            voucherPurchased = True         
        elif(shopAction == 3): # Purchase a booster pack
            obtainedConsumable = True
            showList = True
            shopSlot = random.randint(1, 2)
            lst = list(range(1,6))
            random.shuffle(lst)
            if(random.randint(1, 100) < weightBuyTwoFromPack):
                action = f"ACTION: Purchase the booster pack in slot #{shopSlot}. Select first TWO items in applicable slots from: {lst}"
            else:
                action = f"ACTION: Purchase the booster pack in slot #{shopSlot}. Select first ONE item in applicable slot from: {lst}"            
        elif(shopAction == 4): # Sell a Joker
            if random.randint(1, 100) < weightSellJoker:
                slot = random.randint(1, maxJokerSlots)
                action = f"ACTION: Sell the Joker in slot #{slot}"       
            else: 
                continue     
        elif(shopAction == 5): # Use/Sell a Consumable
            if obtainedConsumable:
                slot = random.randint(1, maxConsumableSlots)
                if(random.randint(1, 100) < weightSellConsumable):
                    action = f"Sell the Consumable in Slot #{slot}"  
                else:
                    action = f"Use the Consumable in Slot #{slot}. If consumable cannot be used now, skip this action"
                    showList = True
            else:
                continue                 
        print(action)
        if(showList):
            print(f"Use the following list to determine card selection order: {cardsInHand}\n")
        input("Press enter to continue once action has completed\n")
        print("\n~~~~~~~~~~~~~~~~~~~\n")
    action = "Exit the shop\n"
    input(action)
    ExitShop()

def ExitShop():
    global weightSkipBlind
    global weightRerollBoss
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if(random.randint(1, 100) < weightRerollBoss):
        input("Reroll the current Boss Blind (if applicable)\n")
    if(random.randint(1, 100) < weightSkipBlind):
        cardsInHand = list(range(1, handSize + 1)) # get list of possible number of cards held in hand, then shuffle them
        random.shuffle(cardsInHand)
        input(f"Skip the current Small or Big blind. Play the Boss Blind. Use the following list if necessary:\n{cardsInHand}\n")
    else:
        input("Play the next blind\n")
    PlayBlind()
    

def rules():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("These are the verbose rules for playing JokeRNG")
    print("1. You *MUST* perform the actions that JokeRNG provides, as provided, in the order provided")
    print("  If any action cannot be completed fully, continue the action up until the point the action cannot be completed, then skip the rest of the action")
    print("    For example, if JokeRNG states to buy 2 Jokers from a Mega Buffoon pack when you only have 1 available Joker slot, take the 1st Joker and skip the rest of the pack")
    print("  If an action cannot be completed, skip the action and continue to the next action")
    print("    For example, if JokeRNG states to buy a Tarot card from a pack, and you have no Consumable slots available, do not buy+use the Tarot, as it *must* be skipped")
    print("2. After each action or series of actions, the program will wait for player input before continuing")
    print("  The program will accept any input and move on as normal. However, there are some special inputs the player can provide (not case sensitive):")
    print("    - win: The player has won the blind, and proceeds to the next shop")
    print("    - lose: The player has lost the blind, and the program should restart from the beginning")
    print("3. When an action is stated, a list of numbers may be provided. This is the order in which, if possible, cards must be selected")
    print("  If the first position in the list does not apply to the current scenario, skip over that number and proceed down the list")
    print("    For example, if JokeRNG states to purchase card 5 from a regular Tarot card pack, skip that number and proceed to the next")
    print("  If the end of the list is reached, and the action has not concluded, loop back to the beginning of the list")
    print("  If the action cannot be completed by selecting any or all of the numebrs on the list, it may be skipped")
    print("  This list will appear in the following scenarios: ")
    print("    - Using a Consumable Card (applies only if Tarot or Spectral card is being used)")
    print("    - Opening a Booster Pack (applies only if Tarot and Spectral pack is being opened)")
    print("4. You may NOT rearrange cards held in hand, Jokers owned, or Consumables owned")
    print("5. If JokeRNG states the player must Discard a hand, and the player has 0 discards remaining, the player MUST instead Play that hand")

class JokeR:

    def __init__(self, root):

        root.title("JokeRNG")

        self.gameState = IntVar()
        self.gameState.set(0)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.step = StringVar() # Current action to take
        self.step.set("Welcome to JokeRNG")

        self.playbtn = StringVar()
        self.playbtn.set("Start New Game")
        ttk.Button(mainframe, text="Calculate Next Action (Blind Won)", command=self.NextGameStateWin).grid(column=1, row=1, sticky=E)
        ttk.Button(mainframe, textvariable=self.playbtn, command=self.NextGameState).grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="Current Action: ").grid(column=3, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.step).grid(column=4, row=1, sticky=W)
        ttk.Button(mainframe, text="Press to Lose", command=self.Exit).grid(column=1, row=2, sticky=E)
        ttk.Button(mainframe, text="Rules", command=self.Rules).grid(column=2, row=2, sticky=W)
        ttk.Label(mainframe, text="Run Variables").grid(column=1, row=3, sticky=E)
        ttk.Label(mainframe, text="Update Before Calculation").grid(column=2, row=3, sticky=W)

        # Calculation Variables
        self.handSize = IntVar()
        self.handSize.set(8)
        self.jokerSize = IntVar()
        self.jokerSize.set(5)
        self.consumableSize = IntVar()
        self.consumableSize.set(2)
        self.shopSize = IntVar()
        self.shopSize.set(2)
        self.ownedJokers = IntVar()
        self.ownedJokers.set(0)
        self.ownedConsumables = IntVar()
        self.ownedConsumables.set(0)

        # Tracking Variables
        self.currentBlind = IntVar()
        self.currentBlind.set(0)
        self.currentAction = IntVar()
        self.currentAction.set(0)

        # Shop Variables
        self.enteredShop = BooleanVar()
        self.enteredShop.set(False)
        self.actionsShop = IntVar()
        self.actionsShop.set(0)
        self.boughtVoucher = BooleanVar()
        self.boughtVoucher.set(False)
        self.currentShopSlots = IntVar()
        self.currentShopSlots.set(2)
        self.currentPackSlots = IntVar()
        self.currentPackSlots.set(2)
        self.shopRerolls = IntVar()
        self.shopRerolls.set(3)

        ttk.Label(mainframe, text="Hand Size: ").grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, textvariable=(self.handSize)).grid(column=2, row=4, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddHandSize).grid(column=3, row=4, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubHandSize).grid(column=4, row=4, sticky=W)

        ttk.Label(mainframe, text="Joker Slots: ").grid(column=1, row=5, sticky=E)
        ttk.Label(mainframe, textvariable=(self.jokerSize)).grid(column=2, row=5, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddJokerSize).grid(column=3, row=5, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubJokerSize).grid(column=4, row=5, sticky=W)

        ttk.Label(mainframe, text="Consumable Slots: ").grid(column=1, row=6, sticky=E)
        ttk.Label(mainframe, textvariable=(self.consumableSize)).grid(column=2, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddConsumeSize).grid(column=3, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubConsumeSize).grid(column=4, row=6, sticky=W)

        ttk.Label(mainframe, text="Shop Slots: ").grid(column=1, row=7, sticky=E)
        ttk.Label(mainframe, textvariable=(self.shopSize)).grid(column=2, row=7, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddShopSize).grid(column=3, row=7, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubShopSize).grid(column=4, row=7, sticky=W)

        ttk.Label(mainframe, text="Owned Jokers: ").grid(column=1, row=8, sticky=E)
        ttk.Label(mainframe, textvariable=(self.ownedJokers)).grid(column=2, row=8, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddOwnedJoker).grid(column=3, row=8, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubOwnedJoker).grid(column=4, row=8, sticky=W)

        ttk.Label(mainframe, text="Owned Consumables: ").grid(column=1, row=9, sticky=E)
        ttk.Label(mainframe, textvariable=(self.ownedConsumables)).grid(column=2, row=9, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddOwnedConsume).grid(column=3, row=9, sticky=(W, E))
        ttk.Button(mainframe, text="-", command=self.SubOwnedConsume).grid(column=4, row=9, sticky=W)


        ttk.Label(mainframe, text="Manually Select Options:").grid(column=1, row=10, sticky=E)
        ttk.Label(mainframe, text="# Items to Pick").grid(column=2, row=10, sticky=(W, E))
        ttk.Label(mainframe, text="# Total Items Available").grid(column=3, row=10, sticky=(W, E))
        ttk.Label(mainframe, text="Output").grid(column=4, row=10, sticky=W)

        self.packText = StringVar()
        self.packText.set("")
        self.packInput = StringVar()
        self.packInput.set("")
        self.packMax = StringVar()
        self.packMax.set("")
        ttk.Button(mainframe, text="Select Cards", command=self.GenerateNumbersOfPackCards).grid(column=1, row=11, sticky=E)
        ttk.Entry(mainframe, width=2, textvariable=self.packInput).grid(column=2, row=11, sticky=(W, E))
        ttk.Entry(mainframe, width=2, textvariable=self.packMax).grid(column=3, row=11, sticky=(W, E))
        ttk.Label(mainframe, textvariable=(self.packText)).grid(column=4, row=11, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def NextGameState(self, *args):
        self.currentAction.set(self.currentAction.get() + 1)
        if(self.gameState.get() == 0): # starting a new game
            self.playbtn.set("Calculate Next Action")
            self.jokerSize.set(5)
            self.handSize.set(8)
            self.consumableSize.set(2)
            self.shopSize.set(2)
            self.ownedJokers.set(0)
            self.ownedConsumables.set(0)
            self.currentAction.set(1)
            # Generate which deck to use
            # Set defaults for variables based on deck chosen
            randomDeck = random.randint(0, 14)
            randomDeck = 13 # TODO testing just with plasma deck
            if(randomDeck == 0):
                self.step.set(f"Action {self.currentAction.get()}: Select the Red Deck")
            elif(randomDeck == 1):
                self.step.set(f"Action {self.currentAction.get()}: Select the Blue Deck")
            elif(randomDeck == 2):
                self.step.set(f"Action {self.currentAction.get()}: Select the Yellow Deck")
            elif(randomDeck == 3):
                self.step.set(f"Action {self.currentAction.get()}: Select the Green Deck")
            elif(randomDeck == 4):
                self.step.set(f"Action {self.currentAction.get()}: Select the Black Deck")
                self.jokerSize.set(6)
            elif(randomDeck == 5):
                self.step.set(f"Action {self.currentAction.get()}: Select the Magic Deck")
                self.ownedConsumables.set(2)
                self.consumableSize.set(3)
            elif(randomDeck == 6):
                self.step.set(f"Action {self.currentAction.get()}: Select the Nebula Deck")
                self.consumableSize.set(1)
            elif(randomDeck == 7):
                self.step.set(f"Action {self.currentAction.get()}: Select the Ghost Deck")
                self.ownedConsumables.set(1)
            elif(randomDeck == 8):
                self.step.set(f"Action {self.currentAction.get()}: Select the Abandoned Deck")
            elif(randomDeck == 9):
                self.step.set(f"Action {self.currentAction.get()}: Select the Checkered Deck")
            elif(randomDeck == 10):
                self.step.set(f"Action {self.currentAction.get()}: Select the Zodiac Deck")
                self.shopSize.set(3)
            elif(randomDeck == 11):
                self.step.set(f"Action {self.currentAction.get()}: Select the Painted Deck")
                self.handSize.set(10)
                self.jokerSize.set(4)
            elif(randomDeck == 12):
                self.step.set(f"Action {self.currentAction.get()}: Select the Anaglyph Deck")
            elif(randomDeck == 13):
                self.step.set(f"Action {self.currentAction.get()}: Select the Plasma Deck")
            elif(randomDeck == 14):
                self.step.set(f"Action {self.currentAction.get()}: Select the Erratic Deck")

            # Go to selecting blind game state
            self.gameState.set(3)

        elif(self.gameState.get() == 1): # currently in a blind
            # Determine whether to Play or Discard, or Sell/Use Jokers/Consumables instead
            # Determine how to Sort
            # Pick up to 5 cards (highly prioritise 5 cards)
            # Display that action

            if random.randint(1, 100) <= (weightSellJoker * self.ownedJokers.get()) and self.ownedJokers.get() > 0: # Randomly sell a Joker, if one is owned
                randJoker = random.randint(1, self.ownedJokers.get())
                self.step.set(f"Action {self.currentAction.get()}: Sell the Joker currently in Slot #{randJoker}")
                self.ownedJokers.set(self.ownedJokers.get() - 1)
            elif random.randint(1, 100) <= weightUseSellConsumable and self.ownedConsumables.get() > 0: # Randomly use or sell a consumable
                randConsumable = random.randint(1, self.ownedConsumables.get())
                if random.randint(1, 100) <= weightSellConsumable:
                    self.step.set(f"Action {self.currentAction.get()}: Sell the Consumable currently in Consumable Slot #{randConsumable}")
                else:
                    self.step.set(f"Action {self.currentAction.get()}: Use the Consumable currently in Consumable Slot #{randConsumable}, if currently possible, otherwise skip this step")
                self.ownedConsumables.set(self.ownedConsumables.get() - 1)
            else: # Play (Or Discard)
                cardsAmount = [1,2,3,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5] # weight heavily for higher amounts played/discarded
                random.shuffle(cardsAmount)
                amountCards = cardsAmount[0]
                lstCards = list(range(1, self.handSize.get() + 1))
                random.shuffle(lstCards)
                sort = "RANK"
                if(random.randint(0,1) == 0): # Coin flip for whether we sort by Suit instead
                    sort = "SUIT"
                playDiscard = "PLAY"
                if(random.randint(1,100) <= weightDiscard):
                    playDiscard = "DISCARD (If able, otherwise Play)"
                CardsToUse = lstCards[0:amountCards]
                CardsToUse.sort()
                self.step.set(f"Action {self.currentAction.get()}: Sort by {sort}, select cards {CardsToUse} left to right, then {playDiscard}")          

        elif(self.gameState.get() == 2): # currently in a shop
            if(self.enteredShop.get() == False): # If first time entering a shop this blind, calculate random number of actions to take this shop
                self.enteredShop.set(True)
                self.actionsShop.set(random.randint(1, maxShopActions))
                self.currentShopSlots.set(self.shopSize.get())
                self.currentPackSlots.set(2)
                self.shopRerolls.set(3)
            self.PickShopAction()
            

        elif(self.gameState.get() == 3): # currently selecting blind
            if(self.currentBlind.get() < 2 and random.randint(1, 100) <= weightSkipBlind):
                self.currentBlind.set(self.currentBlind.get() + 1)
                self.step.set(f"Action {self.currentAction.get()}: Skip the current Blind")
            elif(random.randint(1, 100) <= weightRerollBoss):
                self.step.set(f"Action {self.currentAction.get()}: Reroll the current Boss Blind, if able")
            else:
                self.step.set(f"Action {self.currentAction.get()}: Select the next Blind")
                self.gameState.set(1)

        else: # unhandled
            print("Unhandled game state. Resetting to new game state")
            self.step.set("Unhandled game state. Resetting this run")
            self.gameState.set(0)

    def PickShopAction(self, *args):
        if(self.actionsShop.get() > 0): # Calculate a random shop action
            randShop = random.randint(0,5)

            if randShop == 1 and not self.boughtVoucher.get():
                # Buy Voucher
                self.boughtVoucher.set(True)
                self.step.set(f"Action {self.currentAction.get()}: Purchase the Voucher")

            elif randShop == 2 and self.currentPackSlots.get() > 0:
                # Buy Pack
                randPack = random.randint(1, self.currentPackSlots.get())
                if random.randrange(1, 100) <= weightBuyTwoFromPack:
                    self.step.set(f"Action {self.currentAction.get()}: Purchase the Pack in Pack Slot {randPack}. If a MEGA pack, select 1 option via Manual Selector")
                else:
                    self.step.set(f"Action {self.currentAction.get()}: Purchase the Pack in Pack Slot {randPack}. If a MEGA pack, select 2 options via Manual Selector")
                    self.currentPackSlots.set(self.currentPackSlots.get() - 1)

            elif randShop == 3 and self.shopRerolls.get() > 0:
                # Reroll
                self.shopRerolls.set(self.shopRerolls.get() - 1)
                self.actionsShop.set(self.actionsShop.get() + 1)
                self.step.set(f"Action {self.currentAction.get()}: Reroll the Shop")

            elif randShop == 4 and self.ownedJokers.get() > 0 and random.randint(1, 100) <= (weightSellJoker * self.ownedJokers.get()):
                # Sell a Random Joker
                randJoker = random.randint(1, self.ownedJokers.get())
                self.step.set(f"Action {self.currentAction.get()}: Sell the Joker currently in Slot #{randJoker}")
                self.ownedJokers.set(self.ownedJokers.get() - 1)

            elif randShop == 5 and self.ownedConsumables.get() > 0 and random.randint(1, 100) <= weightUseSellConsumable:
                # Use/Sell Consumable
                randConsumable = random.randint(1, self.ownedConsumables.get())
                if random.randint(1, 100) <= weightSellConsumable:
                    self.step.set(f"Action {self.currentAction.get()}: Sell the Consumable currently in Consumable Slot #{randConsumable}")
                else:
                    self.step.set(f"Action {self.currentAction.get()}: Use the Consumable currently in Consumable Slot #{randConsumable}, if currently possible, otherwise skip this step")
                self.ownedConsumables.set(self.ownedConsumables.get() - 1)
            
            elif (randShop == 0 and self.currentShopSlots.get() > 0) or (self.currentShopSlots.get() > 0):
                # Buy/BuyUse Card From Slot
                if randShop != 0:
                    print("buy item without randshop 0")
                randPurchaseSlot = random.randint(1, self.currentShopSlots.get())
                if random.randint(1, 100) <= weightBuyUse:
                    self.step.set(f"Action {self.currentAction.get()}: Purchase AND USE the Item in Shop Slot {randPurchaseSlot}")
                else:
                    self.step.set(f"Action {self.currentAction.get()}: Purchase the Item in Shop Slot {randPurchaseSlot} WITHOUT USE")
                self.currentShopSlots.set(self.currentShopSlots.get() - 1)

            elif (self.currentShopSlots.get() == 0 and self.boughtVoucher.get() == True and self.currentPackSlots.get() == 0 and self.shopRerolls.get() == 0 and self.ownedConsumables.get() == 0 and self.ownedJokers.get() == 0):
                # Failsale if no possible actions can be taken
                # No Purchaseable items, voucher, or packs. No more rerolls. No Jokers or Consumables to Sell/Use
                self.step(f"Action {self.currentAction.get()}: Somehow, no possible shop actions. Exit this shop.")
                self.gameState.set(3)
                self.enteredShop.set(False)
            else:
                print("Couldn't find anything to do on this shop, exiting this shop")
                self.gameState.set(3)
                self.step.set(f"Action {self.currentAction.get()}: Exit This Shop")
                self.enteredShop.set(False)
            self.actionsShop.set(self.actionsShop.get() - 1)
        else: # If no remaining actions, exit the shop and continue to blind selection
            self.gameState.set(3)
            self.step.set(f"Action {self.currentAction.get()}: Exit This Shop")
            self.enteredShop.set(False)
        
    def NextGameStateWin(self, *args):
        if(self.gameState.get() == 1):
            self.currentBlind.set(self.currentBlind.get() + 1)
            self.currentBlind.set(self.currentBlind.get() % 3)
            if(self.currentBlind.get() == 0): # If entering into the Small Blind shop, reset voucher purchased
                self.boughtVoucher.set(True)
            self.gameState.set(2)
            self.NextGameState()
        else:
            pass

    def GenerateNumbersOfPackCards(self, *args):
        num = int(self.packInput.get())
        max = int(self.packMax.get())
        lst = list(range(1, max+1))
        random.shuffle(lst)
        nums = lst[0:num]
        nums.sort()
        self.packText.set(nums)

    def Rules(self, *args):
        darulez = Toplevel()
        darulez.title = "JokeRNG Rules"
        rulesmainframe = ttk.Frame(darulez, padding="3 3 12 12")
        rulesmainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        darulez.columnconfigure(0, weight=1)
        darulez.rowconfigure(0, weight=1)
        
        ttk.Label(rulesmainframe, text="Here are the essential rules of playing JokeRNG").grid(column=1, row=1, sticky=W)
        ttk.Label(rulesmainframe, text="").grid(column=1, row=2, sticky=W)
        ttk.Label(rulesmainframe, text="1. Actions provided MUST be completed as stated").grid(column=1, row=3, sticky=W)
        ttk.Label(rulesmainframe, text="    If the action stated is impossible, skip the action").grid(column=1, row=4, sticky=W)
        ttk.Label(rulesmainframe, text="2. An action must be completed before proceeding to the next action").grid(column=1, row=5, sticky=W)
        ttk.Label(rulesmainframe, text="3. The player must keep assigned variables accurate").grid(column=1, row=6, sticky=W)
        ttk.Label(rulesmainframe, text="    JokeRNG does attempt to not tell the player to take any impossible actions, but is unaware of what precisely is purchased").grid(column=1, row=7, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. JokeRNG will never tell to use an owned Consumable if no Consumables are owned").grid(column=1, row=8, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If a Negative Joker is purchased, the player must increment the Joker Slots and Owned Jokers by 1 each").grid(column=1, row=9, sticky=W)
        ttk.Label(rulesmainframe, text="4. If an action requires the use of selecting owned cards, use the Manual Selector at the bottom of the main window").grid(column=1, row=10, sticky=W)
        ttk.Label(rulesmainframe, text="    The first input is how many selections must be made. The second input is the total number of possible selections").grid(column=1, row=11, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If an Action tells to use a Death card, input 2 for selections and your current hand size for possible selections").grid(column=1, row=12, sticky=W)
        ttk.Label(rulesmainframe, text="5. You may not perform any actions that JokeRNG does not tell you to perform").grid(column=1, row=13, sticky=W)
        ttk.Label(rulesmainframe, text="    ex. If JokeRNG tells you to purchase a Joker, but you have no empty Joker slots, you may NOT sell a Joker. This action is considered impossible and is thus skipped").grid(column=1, row=14, sticky=W)
        ttk.Label(rulesmainframe, text="6. If an Action tells you to skip a blind, and that skip grants one (or more) packs, you must roll the Manual Selector for the maximum possible selections").grid(column=1, row=15, sticky=W)
        ttk.Label(rulesmainframe, text="    JokeRNG normally tells to pick either 1 or 2 options if a Mega pack is purchased, but has no way of determing if a skipped blind awared a card pack").grid(column=1, row=16, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If a Mega Buffoon Pack skip tag is acquired, you must roll 2 out of 4 to determine which Jokers to choose").grid(column=1, row=17, sticky=W)
        pass

    def Exit(self, *args):
        self.gameState.set(0)
        self.step.set("You're such a joke.")
        self.playbtn.set("Start New Game")

    def AddHandSize(self, *args):
        self.handSize.set(self.handSize.get() + 1)

    def SubHandSize(self, *args):
        self.handSize.set(self.handSize.get() - 1)

    def AddJokerSize(self, *args):
        self.jokerSize.set(self.jokerSize.get() + 1)

    def SubJokerSize(self, *args):
        self.jokerSize.set(self.jokerSize.get() - 1)

    def AddConsumeSize(self, *args):
        self.consumableSize.set(self.consumableSize.get() + 1)

    def SubConsumeSize(self, *args):
        self.consumableSize.set(self.consumableSize.get() - 1)

    def AddShopSize(self, *args):
        self.shopSize.set(self.shopSize.get() + 1)

    def SubShopSize(self, *args):
        self.shopSize.set(self.shopSize.get() - 1)

    def AddOwnedJoker(self, *args):
        self.ownedJokers.set(self.ownedJokers.get() + 1)

    def SubOwnedJoker(self, *args):
        self.ownedJokers.set(self.ownedJokers.get() - 1)

    def AddOwnedConsume(self, *args):
        self.ownedConsumables.set(self.ownedConsumables.get() + 1)

    def SubOwnedConsume(self, *args):
        self.ownedConsumables.set(self.ownedConsumables.get() - 1)


def GuiTest():
    
    #ttk.Button(root, text="Welcome to JokeRNG").grid()
    root = Tk()
    JokeR(root)
    root.mainloop()

if __name__ == "__main__":
    GuiTest()
    #main()