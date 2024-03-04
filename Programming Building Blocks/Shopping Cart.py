foods = []
prices = []
counter = [1]
counter[0] = 0
food_price = -1
full_order = []
#food_count = 0

def add_item():
    food_item = input('Food item:  ')
    food_price = float(input('What does that cost:  '))
    foods.append(food_item)
    prices.append(food_price)
    counter[0] += 1
    print(f'{food_item} has been added to your cart.')

#only function that doesn't work of these
def remove_item():
    print('Which item would you like to remove?')
    print(foods)
    food_item = input()
    number = int(foods.index(food_item))
    foods.pop(number)
    prices.pop(number)
    counter[0] -= 1
    print('The item has been removed.')

def view_cart():
    for x in range(counter[0]):
        print(f'{x + 1}. {foods[x]} - ${prices[x]:.02f}')

def checkout():
    for x in range(counter[0]):
        food_count = int(input(f'How many of the {foods[x]} will you be having?  '))
        full_order.append(food_count)
    tax = float(input('What is the percent sales tax in your area?  '))
    total = 0
    for x in range(counter[0]):
        total = total + (prices[x] * full_order[x])
    total = total * (1 + (tax / 100))
    print(f'Your total is ${total:.02f}')

def complete():
    print('Thank you for shopping with us!  Have a nice day!')
    quit()

def easter_egg():
    print('The person who programmed this is named Benjamin Silver')

def test():
    testing = ['hotdog', 'hamburger', 'chicken']
    counter[0] = 3
    foods.append('hotdog')
    prices.append(1.25)
    foods.append('hamburger')
    prices.append(10.00)
    foods.append('chicken')
    prices.append(3.50)
    take = foods.index('hamburger')
    print(foods)
    print(prices)
    print(take)
    foods.pop(take)
    prices.pop(take)
    counter[0] -= 1
    print(foods)
    print(prices)

while 7 == 7:
    print('What would you like to do?')
    print('1.  Add item to shopping cart')
    print('2.  Remove item from shopping cart')
    print('3.  View cart')
    print('4.  Retrieve checkout total')
    print('5.  Close program')
    action = int(input())

    if action == 1:
        add_item()
    elif action == 2:
        remove_item()
    elif action == 3:
        view_cart()
    elif action == 4:
        checkout()
    elif action == 8:
        test()
    elif action == 47:
        easter_egg()
    else:
        complete()

print(foods)
print(prices)
print(full_order)
