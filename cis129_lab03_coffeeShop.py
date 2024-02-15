#Coffee Shop Lab
#Author: Rylan Carney
#2024-02-12

#Basic greeting, give it a theme
print('Hello! Welcome to Tinycow Coffee,' \
      ' where great things come in tiny packages!')

print('How can I help you today?')

print('Coffee: $5\nMuffin: $4\nCowcoa: $3\nTinycow Limited Figure: $10')
#Should list menu items. Give it a branding to the theme!

#Setting variables for formulas
numCoffee = input('How many cups of coffee would you like?')

numMuffin = input('How many muffins would you like?')

numCowcoa = input('How many cowcoas would you like?')

numFigure = input('How many limited Tinycow figures would you like?')

#Formulas we use this setting
priceCoffee = 5 * (int(numCoffee))

priceMuffin = 4 * (int(numMuffin))

priceCowcoa = 3 * (int(numCowcoa))

priceFigure = 10 * (int(numFigure))

#Constant for Salestax
SALES_TAX = 0.06

#Updated subtotal to include new menu items
subTotal = (int(priceCoffee)) + (int(priceMuffin)) + \
    (int(priceCowcoa)) + (int(priceFigure))

taxRate = (int(subTotal)) * SALES_TAX

grossTotal = (int(subTotal)) + (float(taxRate))

#This will display our receipt. Give it a clean look
print('Tinycow Coffee')

#receipt border/seperator
print('--------------')

print((numCoffee), 'Coffees at $5 each: $', (priceCoffee))

print((numMuffin), 'Muffins at $4 each: $', (priceMuffin))

print((numCowcoa), 'Cowcoas at $3 each: $', (priceCowcoa))

print((numFigure), 'Limited Tinycow Figures at $10 each: $', (priceFigure))

print('6%tax: $', (taxRate))

print('--------------')

print('Total: $',(grossTotal))
#Add a seperator to isolate total. Closing will be after.
#Keep it equal in dashes!

print('--------------')
print('Thank you so much for coming to Tinycow Coffee!')
print('We will always have tinyspot open for you!')
