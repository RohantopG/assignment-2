#here i have used the method of slicing 

value = input("Enter word/number: ")

original = value
processed = value.lower()  
reversed_value = processed[::-1]  

print("\nOriginal:", original)
print("Reversed:", original[::-1])  

if processed == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")
