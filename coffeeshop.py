#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")


#her laget eg den listen som vil apørre brukeren om hvilken type kaffe han vil ha og legge til prisen for for den type kaffe


price = 0
def coffee_list():

   coffee = input("What type of coffee would you like?").title()

   global price

   if coffee=="Espresso":
      price = price + 2.50
   elif coffee=="Americano":
      price = price + 3
   elif coffee=="Latte":
      price = price + 2.50
   elif coffee=="Cappuccino":
      price = price + 3.50
   elif coffee=="Macchiato":
      price = price + 3.50
   elif coffee=="Mocha":
      price = price + 4
   elif coffee=="Flat White":
      price = price + 4
   else:
      print("sorry vi har ikke den type kaffe")
      coffee_list()


coffee_list()



#Complete the code here
# denne delen av koden vil spørre brukeren om copp sturelsen 
# Medium, Large, Extra Large
def size_list():
   global price
   size = input("What size would you like? (Medium, Large, Extra Large)").title()
   if size=="Medium":
      price = price + 0
   elif size=="Large":
      price = price + 0.50
   elif size=="Extra Large":
      price = price + 2


   else:
      print("sorry vi har ikke den storrelsen")
      size_list()


size_list()

# her laget en fonksjon som vil apørre brukern om han vil ta med kaffen eller drikke den på kafeen
def takeaway_list():
   global price
   takeaway = input("vil du drikke her eller ta med?").lower()

   if takeaway=="drikke her":
      price = price + 0
   elif takeaway=="ta med":
      price = price + 1

   else:
         print("sorry vi har ikke den valget")
         takeaway_list()

takeaway_list()



print("----------------------------")
print("Total Cost: £" + str(price))

