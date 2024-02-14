#Coffee Shop Lab
#Author: Rylan Carney



print('Hello! Welcome to Tinycow Coffee,' \
      ' where great things come in tiny packages!')
print('How can I help you today?')
print('Coffee: $5\nMuffin: $4')

numCoffee = input('How many cups of coffee would you like?')

numMuffin = input('How many muffins would you like?')


priceCoffee = 5 * (int(numCoffee))

priceMuffin = 4 * (int(numMuffin))

SALES_TAX = 0.06

subTotal = (int(priceCoffee)) + (int(priceMuffin))

taxRate = (int(subTotal)) * SALES_TAX

grossTotal = (int(subTotal)) + (float(taxRate))


print('Tinycow Coffee')

print('--------------')

print((numCoffee), 'Coffees at $5 each: $', (priceCoffee))

print((numMuffin), 'Muffins at $4 each: $', (priceMuffin))

print('6%tax: $', (taxRate))

print('--------------')

print('Total: $',(grossTotal))

