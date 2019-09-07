def cheese_and_crackers(cheese_count, boxes_of_crackers):   #function 
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")   #print 

def noSenseFunction(cheese_count, boxes_of_crackers):
    print(f"HI! {cheese_count} , {cheese_and_crackers}")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #function call with integer argument


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)   #function call with variables argument


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

noSenseFunction(20, 50)
noSenseFunction(1+2, 50)
noSenseFunction(50, 6+7)
noSenseFunction(amount_of_cheese, amount_of_crackers)
noSenseFunction(amount_of_cheese+6, amount_of_crackers+7)
noSenseFunction(amount_of_cheese, 23)
noSenseFunction(43, amount_of_crackers)
noSenseFunction(43+5, amount_of_crackers)
noSenseFunction(amount_of_cheese, 5+6)
noSenseFunction(amount_of_cheese+4, amount_of_crackers+5)