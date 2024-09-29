print ("Hello, Welcome to Micho Supermarkets")
print ("This is the billing page for the items you want to buy.")
print ("""Item ID's for the items are - 
       1 - Potato
       2 - Carrot
       3 - Onion
       4 - Brinjal
       5 - Beans
       6 - Cabbage
       7 - Cauliflower
       8 - Apple
       9 - Banana
       10 - Tomato
       11 - Capsicum
       12 - Orange
       13 - Mango """)
item1 = int = input ("Type your item no. of the item that you want to bill :")
if item1 == "1":
   print("Price of Potatoes per kg is ₹25")
   item1amt = float(input("Type in the amount of Potato(in Kgs) you want1"))
   print("Price of your Potatoes are" , item1amt * 25)
elif item1 == "2":
   print("Price of Carrot per kg is ₹40")
   item1amt = float(input("Type in the amount of Carrot(in Kgs) you want"))
   print("Price of your Carrots are" , item1amt * 40)
elif item1 == "3":
   print("Price of Onions per kg is ₹33")
   item1amt = float(input("Type in the amount of Onion(in Kgs) you want"))
   print("Price of your Onions are" , item1amt * 33)
elif item1 == "4":
   print("Price of Brinjal per kg is ₹20")
   item1amt = float(input("Type in the amount of Brinjal(in Kgs) you want"))
   print("Price of your Brinjal is" , item1amt * 20)
elif item1 == "5":
   print("Price of Beans per kg is ₹30")
   item1amt = float(input("Type in the amount of Beans(in Kgs) you want"))
   print("Price of your Beans are" , item1amt * 30)
elif item1 == "6":
   print("Price of Cabbage per kg is ₹18")
   item1amt = float(input("Type in the amount of Cabbage(in Kgs) you want"))
   print("Price of your Cabbage is" , item1amt * 18)
elif item1 == "7":
   print("Price of Cauliflower per kg is ₹22")
   item1amt = float(input("Type in the amount of Cauliflower(in Kgs) you want"))
   print("Price of your Cauliflower is" , item1amt * 22)
elif item1 == "8":
   print("Price of Apples per kg is ₹150")
   item1amt = float(input("Type in the amount of Apple(in Kgs) you want"))
   print("Price of your Apples are" , item1amt * 150)
elif item1 == "9":
   print("Price of Bananas per kg is ₹50")
   item1amt = float(input("Type in the amount of Banana(in Kgs) you want"))
   print("Price of your Bananas are" , item1amt * 50)
elif item1 == "10":
   print("Price of Tomatoes per kg is ₹40")
   item1amt = float(input("Type in the amount of Tomato(in Kgs) you want"))
   print("Price of your Tomatoes are" , item1amt * 40)
elif item1 == "11":
   print("Price of Capsicums per kg is ₹45")
   item1amt = float(input("Type in the amount of Capsicum(in Kgs) you want"))
   print("Price of your Capsicums are" , item1amt * 45)
elif item1 == "12":
   print("Price of Oranges per kg is ₹60")
   item1amt = float(input("Type in the amount of Orange(in Kgs) you want"))
   print("Price of your Oranges are" , item1amt * 60)
elif item1 == "13":
   print("Price of Mangoes per kg is ₹500")
   item1amt = float(input("Type in the amount of Mango(in Kgs) you want"))
   print("Price of your Mangoes are" , item1amt * 500)
else:
   print("Invalid Item number typed. Re-run program again")