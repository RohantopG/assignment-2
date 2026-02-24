# here to split the number i am taking the variabhles and  input.
total_bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

#here i am using maths formula to calculate the tax and tip and total amount and per person amount.
subtotal = total_bill
tax_amount = subtotal * (tax_percent / 100)
after_tax = subtotal + tax_amount
tip_amount = after_tax * (tip_percent / 100)
total = after_tax + tip_amount
per_person = total / people

print("\n.... BILL BREAKDOWN ....")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
print(f"After tax: ₹{after_tax:.2f}")
print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
print(f"Total: ₹{total:.2f}")
print(f"Per person: ₹{per_person:.2f}")
