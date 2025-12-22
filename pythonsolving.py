#Develop a Python program that accepts a user's total purchase amount. Implement the following logic using conditional statements (if-elif-else):
#If the amount is greater than 5000, apply a 20% discount.
#If the amount is between 2000 and 5000, apply a 10% discount.
#Otherwise, no discount is applied.
#Constraint: The program must display the original amount, the discount amount, and the final price to be paid.

amt=int(input("Enter a Amount:"))
print("Your Original Amount is:",amt)
if(amt>5000):
    disc=amt*0.20
    amt=amt-disc
    print("After 20% Discount Your amount is",amt)
elif 2000<amt<5000:
    disc=amt*0.10
    amt=amt-disc
    print("After 10% Discount total amount is",amt)
else:
    print("No Discount")
