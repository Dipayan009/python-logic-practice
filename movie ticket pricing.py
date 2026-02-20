age=int(input("enter your age:"))
day=input("enter the day in lower case:").lower()
if (age<12):
    price=100
elif(age<=59):
    price=200
else:
    price=150
    
if(day=="sunday"):
   finalprice= price+50
else:
   finalprice = price
print("your final price:",finalprice)