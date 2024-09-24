inventory = []
try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  f = open("inventory.txt", "w")
  f.close()

def add():
  item = input("Input the item to add: > ")
  inventory.append(item.capitalize())
  print(f"{item.capitalize()} has been added to your inventory.")

def remove():
  item = input("Input the item to remove: > ")
  if item.capitalize() in inventory:
    inventory.remove(item.capitalize())
    print(f"{item.capitalize()} has been removed from your inventory.")
  else:
    print("Item is not in inventory")

def view():
  item = input("Input the item to view: > ")
  if item.capitalize() in inventory:
    print(f"You have {inventory.count(item.capitalize())} {item.capitalize()}")
  else:
    print("Item is not in inventory")

while True:
  print()
  menu = input("1: Add  2: Remove  3: View  > ")
  if menu == "1":
    add()
  elif menu == "2":
    remove()
  elif menu == "3":
    view()
  else:
    print("Invalid input")
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()