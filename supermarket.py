from datetime import datetime

name = input("Enter your name: ")

# Lists of items available in the supermarket
lists = '''
Rice Rs 20/kg
Sugar Rs 40/kg
Salt Rs 10/kg
Tea Rs 50/kg
Coffee Rs 100/kg
Paneer Rs 200/kg
Oil Rs 150/ltr
Milk Rs 50/ltr
Maggie Rs 20/pack
Boost Rs 100/pack
Colgate Rs 50/pack
'''

# Rates of items available in the supermarket
items = {
    'Rice': 20,
    'Sugar': 40,
    'Salt': 10,
    'Tea': 50,
    'Coffee': 100,
    'Paneer': 200,
    'Oil': 150,
    'Milk': 50,
    'Maggie': 20,
    'Boost': 100,
    'Colgate': 50
}

# Initialize variables
Totalprice = 0
ilist = []
qlist = []
plist = []

# Display the list of items
option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)

while True:
    inp1 = int(input("If you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter the item: ")
        if item in items:
            quantity = int(input("Enter the quantity: "))
            Price = quantity * items[item]
            Totalprice += Price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(Price)
        else:
            print("Item not available")
    else:
        print("Invalid input")

# Calculate GST and Final Price
gst = Totalprice * 5 / 100
Finalprice = Totalprice + gst

# Print the bill
inp = input("Can I give you a check yes/no: ")
if inp == 'yes':
    print(25 * "=", "John's Supermarket", 25 * "=")
    print(28 * " ", "Nellore")
    print("Name:", name, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print(f"{'S NO':<10}{'Item':<20}{'Quantity':<15}{'Price':>10}")
    print(75 * "-")
    for i in range(len(ilist)):
        print(f"{i + 1:<10}{ilist[i]:<20}{qlist[i]:<15}{plist[i]:>10}")
    print(75 * "-")
    print(f"{'Total Price:':<50}{Totalprice:>10}")
    print(f"{'GST:':<50}{gst:>10}")
    print(75 * "-")
    print(f"{'Final Price:':<50}{Finalprice:>10}")
    print(75 * "-")
    print(f"{'Thank you for shopping':^75}")
    print(75 * "-")