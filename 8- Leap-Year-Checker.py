# i take the input of the year
year = int(input("Enter a year: "))

#i am calculating the leap year using the if else first i check wheather where the year is leap yeaer by dividing by 4 and dividing by 100 it should not be equal to  0
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"\n{year} is a Leap Year.")
    
    if year % 400 == 0:
        print("Reason: Divisible by 400.")
    elif year % 100 == 0:
        print("Reason: Divisible by 100 but also divisible by 400 condition satisfied.")
    else:
        print("Reason: Divisible by 4 and not divisible by 100.")
else:
    print(f"\n{year} is NOT a Leap Year.")
    
    if year % 4 != 0:
        print("Reason: Not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but NOT divisible by 400.")
