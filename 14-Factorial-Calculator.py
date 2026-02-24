# for factorial calculation i have taken the input 

num = int(input("Enter a number: "))

#here i have handled the edge case for zero
if num == 0:
    print("0! = 1")

else:
    factorial = 1
    steps = ""

    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i)
        if i != 1:
            steps += " × "

    print(f"{num}! = {steps} = {factorial}")
