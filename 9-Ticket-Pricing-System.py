#i am takinbg age day and ticket.
age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# according to age i am classifing the amount.
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# here i saw the days in which the amount was discounted and if those days appear then i applyed discount of 2o percent
if day in ["friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

# Calculations
total_base = base_price * tickets
discount_amount = total_base * (discount_percent / 100)
final_amount = total_base - discount_amount


print("\n.... TICKET BILL ....")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Number of tickets:", tickets)
print("Total base price: ₹{:.2f}".format(total_base))
print("Discount: {}%".format(discount_percent))
print("Discount amount: ₹{:.2f}".format(discount_amount))
print("Final amount to pay: ₹{:.2f}".format(final_amount))
