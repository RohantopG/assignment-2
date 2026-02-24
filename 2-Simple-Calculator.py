
#here first i took two variables no1 and no2
#it will take input from the user 

no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))

print("\nResults:")


print(f"{no1} + {no2} = {no1 + no2}")


print(f"{no1} - {no2} = {no1 - no2}")


print(f"{no1} * {no2} = {no1 * no2}")


#here the any number cant be divided by zero.
if no2 != 0:
    print(f"{no1} / {no2} = {round(no1 / no2, 2)}")
else:
    print("Division by zero is not allowed")


if no2 != 0:
    print(f"{no1} % {no2} = {no1 % no2}")
else:
    print("Modulus by zero is not allowed")


print(f"{no1} ^ {no2} = {no1 ** no2}")
