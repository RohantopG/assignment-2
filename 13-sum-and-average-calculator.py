# here i am calculating sum and average i waill take input and then i will keep thta input in forloop untill the count

count = int(input("How many numbers? "))

numbers = []

for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print("\nResults:")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
