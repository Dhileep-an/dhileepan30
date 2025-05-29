#HOTEL FOOD MENU
menu = {"idli": 3.00,
         "2 puri": 4.50,
       "pongal": 6.00,
       "chapati": 2.50,
           "chips": 1.00,
          "dosa": 3.50,
       "soda": 3.00,
           "2 biscuits": 4.25,
           "voda": 1.45,
           "samosa":1.35,
         "parotta":4.35}
cart = []
total = 0

print("--------- _ FOOD MENU _ ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------------")

while True:
    food = input("Select an FOOD you want (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")

print("-------------THANK YOU--------------")
print("--------**COME AGAIN LATER**--------")
