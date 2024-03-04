import math

items = int(input("How many items are there? "))
item_boxes = int(input("How many items are you going to put into each box? "))

boxes = math.ceil(items / item_boxes)

print(f"If you have {items} items, and you are putting {item_boxes} in each box, you will need at least {boxes} boxes to fill this order.")
