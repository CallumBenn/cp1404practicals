

# get number_of_items
# for i in number_of_items
#     total_price = total_price + item_price
# if total_price > 100
#     total_price = total_price * 0.90
# print total_price

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    number_of_items = int(input("Invalid number of items! \nNumber of items: "))
for i in range(number_of_items):
    total_price = total_price + float(input("Price of item: "))
if total_price > 100:
    total_price = total_price * 0.90
print(f"Total price for 3 items is ${total_price:.2f}")
