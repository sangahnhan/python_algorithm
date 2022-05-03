import random
LENGTH = 8
string_pool ="0123456789"
shipment = ""
for i in range(LENGTH):
    shipment +=random.choice(string_pool)

print(shipment)
