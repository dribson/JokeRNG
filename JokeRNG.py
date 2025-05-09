import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
import json

handSize = 8
maxJokerSlots = 5
maxConsumableSlots = 2
maxShopSlots = 2
defaultDeck = 0
alwaysFiveCards = False

maxShopActions = 5
maxShopRolls = 3
weightSkipBlind = 10
weightRerollBoss = 10
weightBuyUse = 50
weightBuyTwoFromPack = 50
weightSellJoker = 30
weightUseSellConsumable = 40
weightSellConsumable = 20
weightDiscard = 45


class JokeR:

    def __init__(self, root):

        f = font.nametofont('TkTextFont')
        f.configure(size=18)

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
        ttk.Button(mainframe, text="Calculate Next Action (Blind Won)", command=self.NextGameStateWin).grid(column=1, row=1, sticky=(N,S,E))
        ttk.Button(mainframe, textvariable=self.playbtn, command=self.NextGameState).grid(column=2, row=1, sticky=(N,S,W,E))
        ttk.Label(mainframe, text="Current Action: ", font=f).grid(column=3, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.step, font=f).grid(column=4, row=1, sticky=W)
        ttk.Button(mainframe, text="Press to Lose", command=self.Exit).grid(column=1, row=2, sticky=(N,S,E))
        ttk.Button(mainframe, text="Rules", command=self.Rules).grid(column=2, row=2, sticky=(N,S,W))
        ttk.Label(mainframe, text="Run Variables", font=f).grid(column=1, row=3, sticky=E)
        ttk.Label(mainframe, text="Update Before Calculation", font=f).grid(column=2, row=3, sticky=W)

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

        ttk.Label(mainframe, text="Hand Size: ", font=f).grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, textvariable=(self.handSize), font=f).grid(column=2, row=4, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddHandSize).grid(column=3, row=4, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubHandSize).grid(column=4, row=4, sticky=(N,S,W))

        ttk.Label(mainframe, text="Joker Slots: ", font=f).grid(column=1, row=5, sticky=E)
        ttk.Label(mainframe, textvariable=(self.jokerSize), font=f).grid(column=2, row=5, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddJokerSize).grid(column=3, row=5, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubJokerSize).grid(column=4, row=5, sticky=(N,S,W))

        ttk.Label(mainframe, text="Consumable Slots: ", font=f).grid(column=1, row=6, sticky=E)
        ttk.Label(mainframe, textvariable=(self.consumableSize), font=f).grid(column=2, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddConsumeSize).grid(column=3, row=6, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubConsumeSize).grid(column=4, row=6, sticky=(N,S,W))

        ttk.Label(mainframe, text="Shop Slots: ", font=f).grid(column=1, row=7, sticky=E)
        ttk.Label(mainframe, textvariable=(self.shopSize), font=f).grid(column=2, row=7, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddShopSize).grid(column=3, row=7, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubShopSize).grid(column=4, row=7, sticky=(N,S,W))

        ttk.Label(mainframe, text="Owned Jokers: ", font=f).grid(column=1, row=8, sticky=E)
        ttk.Label(mainframe, textvariable=(self.ownedJokers), font=f).grid(column=2, row=8, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddOwnedJoker).grid(column=3, row=8, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubOwnedJoker).grid(column=4, row=8, sticky=(N,S,W))

        ttk.Label(mainframe, text="Owned Consumables: ", font=f).grid(column=1, row=9, sticky=E)
        ttk.Label(mainframe, textvariable=(self.ownedConsumables), font=f).grid(column=2, row=9, sticky=(W, E))
        ttk.Button(mainframe, text="+", command=self.AddOwnedConsume).grid(column=3, row=9, sticky=(N, S, W, E))
        ttk.Button(mainframe, text="-", command=self.SubOwnedConsume).grid(column=4, row=9, sticky=(N,S,W))


        ttk.Label(mainframe, text="Manually Select Options:", font=f).grid(column=1, row=10, sticky=E)
        ttk.Label(mainframe, text="# Items to Pick", font=f).grid(column=2, row=10, sticky=(W, E))
        ttk.Label(mainframe, text="# Total Items Available").grid(column=3, row=10, sticky=(W, E))
        ttk.Label(mainframe, text="Output").grid(column=4, row=10, sticky=W)

        self.packText = StringVar()
        self.packText.set("")
        self.packInput = StringVar()
        self.packInput.set("")
        self.packMax = StringVar()
        self.packMax.set("")
        ttk.Button(mainframe, text="Select Cards", command=self.GenerateNumbersOfPackCards).grid(column=1, row=11, sticky=(N, S, E))
        ttk.Entry(mainframe, width=2, textvariable=self.packInput, font=f).grid(column=2, row=11, sticky=(W, E))
        ttk.Entry(mainframe, width=2, textvariable=self.packMax, font=f).grid(column=3, row=11, sticky=(W, E))
        ttk.Label(mainframe, textvariable=(self.packText), font=f).grid(column=4, row=11, sticky=W)

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
            randomDeck = random.randint(1, 15)
            if (0 < defaultDeck < 16):
                randomDeck = defaultDeck
            if(randomDeck == 1):
                self.step.set(f"Action {self.currentAction.get()}: Select the Red Deck")
            elif(randomDeck == 2):
                self.step.set(f"Action {self.currentAction.get()}: Select the Blue Deck")
            elif(randomDeck == 3):
                self.step.set(f"Action {self.currentAction.get()}: Select the Yellow Deck")
            elif(randomDeck == 4):
                self.step.set(f"Action {self.currentAction.get()}: Select the Green Deck")
            elif(randomDeck == 5):
                self.step.set(f"Action {self.currentAction.get()}: Select the Black Deck")
                self.jokerSize.set(6)
            elif(randomDeck == 6):
                self.step.set(f"Action {self.currentAction.get()}: Select the Magic Deck")
                self.ownedConsumables.set(2)
                self.consumableSize.set(3)
            elif(randomDeck == 7):
                self.step.set(f"Action {self.currentAction.get()}: Select the Nebula Deck")
                self.consumableSize.set(1)
            elif(randomDeck == 8):
                self.step.set(f"Action {self.currentAction.get()}: Select the Ghost Deck")
                self.ownedConsumables.set(1)
            elif(randomDeck == 9):
                self.step.set(f"Action {self.currentAction.get()}: Select the Abandoned Deck")
            elif(randomDeck == 10):
                self.step.set(f"Action {self.currentAction.get()}: Select the Checkered Deck")
            elif(randomDeck == 11):
                self.step.set(f"Action {self.currentAction.get()}: Select the Zodiac Deck")
                self.shopSize.set(3)
            elif(randomDeck == 12):
                self.step.set(f"Action {self.currentAction.get()}: Select the Painted Deck")
                self.handSize.set(10)
                self.jokerSize.set(4)
            elif(randomDeck == 13):
                self.step.set(f"Action {self.currentAction.get()}: Select the Anaglyph Deck")
            elif(randomDeck == 14):
                self.step.set(f"Action {self.currentAction.get()}: Select the Plasma Deck")
            elif(randomDeck == 15):
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
                if(str.lower(alwaysFiveCards) == "true"):
                    cardsAmount = [5]
                    print("True")
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
                    self.step.set(f"Action {self.currentAction.get()}: Purchase (Consumable: AND USE) the Item in Shop Slot {randPurchaseSlot}")
                else:
                    self.step.set(f"Action {self.currentAction.get()}: Purchase (Consumable: WITHOUT USE) the Item in Shop Slot {randPurchaseSlot}")
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

        
        f = font.nametofont('TkTextFont')
        f.configure(size=18)
        
        ttk.Label(rulesmainframe, text="Here are the essential rules of playing JokeRNG", font=f).grid(column=1, row=1, sticky=W)
        ttk.Label(rulesmainframe, text="").grid(column=1, row=2, sticky=W)
        ttk.Label(rulesmainframe, text="1. Actions provided MUST be completed as stated", font=f).grid(column=1, row=3, sticky=W)
        ttk.Label(rulesmainframe, text="    If the action stated is impossible, skip the action", font=f).grid(column=1, row=4, sticky=W)
        ttk.Label(rulesmainframe, text="2. An action must be completed before proceeding to the next action", font=f).grid(column=1, row=5, sticky=W)
        ttk.Label(rulesmainframe, text="3. The player must keep assigned variables accurate", font=f).grid(column=1, row=6, sticky=W)
        ttk.Label(rulesmainframe, text="    JokeRNG does attempt to not tell the player to take any impossible actions, but is unaware of what precisely is purchased", font=f).grid(column=1, row=7, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. JokeRNG will never tell to use an owned Consumable if no Consumables are owned", font=f).grid(column=1, row=8, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If a Negative Joker is purchased, the player must increment the Joker Slots and Owned Jokers by 1 each", font=f).grid(column=1, row=9, sticky=W)
        ttk.Label(rulesmainframe, text="4. If an action requires the use of selecting owned cards, use the Manual Selector at the bottom of the main window", font=f).grid(column=1, row=10, sticky=W)
        ttk.Label(rulesmainframe, text="    The first input is how many selections must be made. The second input is the total number of possible selections", font=f).grid(column=1, row=11, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If an Action tells to use a Death card, input 2 for selections and your current hand size for possible selections", font=f).grid(column=1, row=12, sticky=W)
        ttk.Label(rulesmainframe, text="5. You may not perform any actions that JokeRNG does not tell you to perform", font=f).grid(column=1, row=13, sticky=W)
        ttk.Label(rulesmainframe, text="    ex. If JokeRNG tells you to purchase a Joker, but you have no empty Joker slots, you may NOT sell a Joker. This action is considered impossible and is thus skipped", font=f).grid(column=1, row=14, sticky=W)
        ttk.Label(rulesmainframe, text="6. If an Action tells you to skip a blind, and that skip grants one (or more) packs, you must roll the Manual Selector for the maximum possible selections", font=f).grid(column=1, row=15, sticky=W)
        ttk.Label(rulesmainframe, text="    JokeRNG normally tells to pick either 1 or 2 options if a Mega pack is purchased, but has no way of determing if a skipped blind awared a card pack", font=f).grid(column=1, row=16, sticky=W)
        ttk.Label(rulesmainframe, text="        ex. If a Mega Buffoon Pack skip tag is acquired, you must roll 2 out of 4 to determine which Jokers to choose", font=f).grid(column=1, row=17, sticky=W)
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


def RunJokeRNG():
    root = Tk()
    JokeR(root)
    root.mainloop()

def LoadJson():
    with open('config.json', 'r') as config_file:
        data = json.load(config_file)
    global maxShopActions, maxShopRolls, defaultDeck, alwaysFiveCards, weightSkipBlind, weightRerollBoss, weightBuyUse, weightBuyTwoFromPack, weightSellJoker, weightUseSellConsumable, weightSellConsumable, weightDiscard

    maxShopActions = data['maxShopActions'] # Maximum number of possible actions to take per shop, excluding rerolls
    maxShopRolls = data['maxShopRolls'] # Maximum number of possible rerolls per shop
    defaultDeck = data['defaultDeck'] # Which deck to pick, ranging from 1-15. Leave as 0 for random deck. Red Deck = 1, Blue Deck = 2, Erratic Deck = 15, etc.
    alwaysFiveCards = data['alwaysFiveCards'] # If the tool should always pick 5 cards when playing or discarding a hand.
    weightSkipBlind = data['weightSkipBlind'] # Percent chance to skip a Small or Big Blind
    weightRerollBoss = data['weightRerollBoss'] # Percent chance to reroll a Boss Blind (if available)
    weightBuyUse = data['weightBuyUse'] # Percent chance to Buy+Use a Consumable from the shop, instead of just buying it
    weightBuyTwoFromPack = data['weightBuyTwoFromPack'] # Percent chance to take 2 cards from a Mega pack purchased from the shop
    weightSellJoker = data['weightSellJoker'] # Percent chance, per owned Joker, to sell an owned Joker as any action
    weightUseSellConsumable = data['weightUseSellConsumable'] # Percent chance to Use or Sell a currently owned Consumable as any action
    weightSellConsumable = data['weightSellConsumable'] # Percent chance to Sell a Consumable instead of using
    weightDiscard = data['weightDiscard'] # Percent chance to Discard and Hand instead of Playing it

if __name__ == "__main__":
    LoadJson()
    RunJokeRNG()