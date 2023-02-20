gross = int(input("How much do you earn"))
if gross > 4000:
    inc_tax = 0.18
elif gross > 2000 and gross <=4000:
    inc_tax = 0.14
elif gross > 1000 and gross <=2000:
    inc_tax = 0.12
else:
    inc_tax = 0.1
Children = int(input("How many children do you have"))
if gross < 2000:
    c_tax = inc_tax - (Children*0.01)
else:
    c_tax = inc_tax - (Children*0.005)
Net = gross - (gross*c_tax)
print ("Your net salary corresponds to the amount of", Net, "euros")

