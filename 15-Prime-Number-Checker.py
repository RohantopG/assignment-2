# to check the prime number i have taken the input from the user and checked wheather its prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a prime number")

elif num == 2:
    print("2 is a PRIME number")

else:
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")
