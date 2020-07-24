x=float(input("Enter the auto price:"))
y=float(input("Enter the price of the paper:"))
a=150
b=50
r=((float(input("Enter The inflation rate:")))/100)
z=(a*x+y*b)
f=(z*r)+z
print("Increase the cost of the company:",f)