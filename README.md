# JokeRNG
A silly little program that tells you how to play Balatro, entirely dictated by RNG

## Info
Want to play Balatro, without any of the strenuous thinking involved. JokeRNG is the tool for you! JokeRNG will tell you exactly which action to take at the click of a button. This tool does *not* hook into Balatro in any way, shape, or form, some some information must be kept updated manually.

JokeRNG was developed since my brother wanted to experiment with playing Balatro where everything is random. I developed a command line version of this tool, but decided I wanted it to look better, after which I turned this into a GUI program via TKinter library. The command line version is still in the code, but inaccessable and not up to date.

## How to Use
This has only been tested on Windows. To run, open Command Prompt or Powershell, and run the command **python .\JokeRNG.py**

Press the **Start New Game** button to start a game of Balatro. The action to take is then displayed in the top right corner of the application.

Press the **Calculate Next Action** button to continue on to the next action. Any action must be completed as stated before continuing to the next action.

When you win a blind in Balatro, click the **Calculate Next Action (Blind Won)** button. This will continue the application into the shop phase.

If an action requires the use of selecting cards, such as using a Tarot Card or opening a Pack, use the **Manual Card Selector** at the bottom of the application to determine which selections are to be made

## Configuration
The app comes with a configuation file 'config.json' that allows for some amount of customization in terms of how likely certain actions are to occur.

**maxShopActions**: The maximum number of actions to take per shop. This excludes rerolling the shop. The total actions per shop will be randomized between 1 and this number. *Default*: 5

**maxShopRolls**: The maximum number of times a shop can be rerolled. This does not use an action. The total number of rerolls per shop will be randomized between 0 and this number. *Default*: 3

**defaultDeck**: If this is set between 1 and 15, will pick the associated deck. See the [Balatro Wiki](https://balatrogame.fandom.com/wiki/Decks) page for a refresher. Otherwise, picks a random deck out of all 15. *Default*: 0

**weightSkipBlind**: The percent chance that the Small Blind or the Big Blind must be skipped. *Default*: 10

**weightRerollBoss**: The percent chance that the Boss Blind must be rerolled, if currently able. Does not include situation where the current Blind Skip Tag is Reroll Boss Tag. *Default*: 10

**weightBuyUse**: The percent chance that a Consumable must be used from the Shop when purchased. Does not affect Jokers or Playing Cards purchased from the shop. *Default*: 50

**weightBuyTwoFromPack**: The percent chance that only 1 option may be selected if a Mega pack is purchased from a shop. Does not include situations where a Mega pack is acquired from a Skip Tag. *Default*: 50

**weightSellJoker**: The percent chance, per owned Joker, to sell a random Joker. Can be rolled as any action, in the shop or during a round. *Default*: 3

**weightUseSellConsumable**: The percent chance that an owned Consumable can be Used or Solt. Can be rolled as any action, in the shop or during a round. *Default*: 40

**weightSellConsumable**: The percent chance that an owned Consumable must be sold instead of played. Only occurs if *weightUseSellConsumable* is successfully rolled. *Default*: 20

**weightDiscard**: The percent chance that a hand must be Discarded instead of Played. *Default*:45