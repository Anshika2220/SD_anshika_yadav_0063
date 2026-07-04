menu = {"Cold Coffee":"100",
        "maggie":"80"
        "pasta":"400"
        "Pizza":"300"
        "tea":"20"
        "spring roll":"200"
        }
print("Welcome to Hazlenut Factory")
print(menu)
amount=0
order=input('what you wish to order')
if order in menu:
  amount += menu[order]
else:
  print("not available")
another_order = input("if you wish to order something else ?")
if another_order=="yes":
    if order in menu:
       amount += menu[order]
    else:
       print("not available")
print("the total amount of order is (amount)")
