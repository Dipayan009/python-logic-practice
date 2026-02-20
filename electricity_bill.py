units = int(input("Enter the units "))
bill = 0
if (units<= 100):
    bill = units * 5
elif (units<= 200):
    bill = ((100*5)+((units - 100)*7))
else:
    bill =((100*5)+(100*7)+((units - 200)*10))

if (bill > 1000):
    surcharge = bill * 10/100
    bill = bill + surcharge
print("Final electricity bill= ", bill)