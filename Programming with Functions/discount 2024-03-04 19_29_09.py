from datetime import date

tax = .06
today = (date.weekday(date.today())) + 1
print(today)
##0 = Sunday
##6 = Saturday

def discount_calc(subtotal):
    if ((today == 2) or (today == 3)):
        if (subtotal >= 50):
            discount = 0.90
            print("Thank you for shopping with us today!")
            print("As this purchase exceeds $50, you qualify for")
            print("our deal of the day!")
            print("You will receive a discount of one tenth of")
            print('your purchase discounted today!')
        else:
            under_pay = 50 - subtotal
            print("We do have a discount of the day, but you need to spent at least $50 to qualify")
            print(f"As of right now, you are ${under_pay} shy of $50")
            discount = 1
    else:
        discount = 1
        
    return discount

def main(subtotal):
    
    discount = discount_calc(subtotal)
    print(f"Given that your subtoal is: {subtotal}")
    if discount < 1:
        subtotal *= discount
        print(f"After your discount, your new subtotal is: {subtotal}")
    total_tax = round((subtotal * tax), 2)
    print(f"Given the tax of 6 Percent, the tax for this purchase is: ${total_tax}")
    total_bill = round((subtotal + total_tax), 2)
    print(f"Thus, your final bill is ${total_bill}")
    subtotal = round(float(input('As a decimal, what is your new subtotal? (Type "0" to end".) ')), 2)
    return subtotal

subtotal = round(float(input("As a decimal, what is your subtotal? ")), 2)

while subtotal != 0:
    subtotal = main(subtotal)

