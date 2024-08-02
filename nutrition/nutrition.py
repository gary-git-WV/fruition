''' Solution for CS50P Week 2 PSet2 "Nutrition Facts"'''
def main():
    '''Use dictionary for fruit nutrition info'''
    fruits ={
    "Apple": "130", "Avocado":	"50", "Banana":	"110",
    "Cantaloupe": "50", "Grapefruit": "60", "Grapes": "90",
    "Honeydew Melon": "50", "Kiwifruit": "90", "Lemon": "15",
    "Lime": "20", "Nectarine":	"60", "Orange":	"80", "Peach":	"60",
    "Pear":	"100", "Pineapple":	"50", "Plums":	"70", "Strawberries":	"50",
    "Sweet Cherries":	"100", "Tangerine":	"50", "Watermelon":	"80"
    }
    # Get user input of fruit name, correcting case to Title case
    k = input("Item:").title()
    # If the input is in the fruit dictionary, print calories
    if k in fruits:
        print("Calories:", fruits[k])
main()
