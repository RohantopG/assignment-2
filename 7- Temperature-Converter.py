while True:
    print("\n----= TEMPERATURE CONVERTER ----")
    print("1. Celsius to Fahreheit")
    print("2. Fahreheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahreheit to Kelvin")
    print("6. Kelvin to Fahreheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting program...")
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        temp = float(input("Enter temperature value: "))

        if choice == '1':
            result = (temp * 9/5) + 32
            print(f"{temp}°C = {result:.2f}°F")

        elif choice == '2':
            result = (temp - 32) * 5/9
            print(f"{temp}°F = {result:.2f}°C")

        elif choice == '3':
            result = temp + 273.15
            print(f"{temp}°C = {result:.2f}K")

        elif choice == '4':
            result = temp - 273.15
            print(f"{temp}K = {result:.2f}°C")

        elif choice == '5':
            result = (temp - 32) * 5/9 + 273.15
            print(f"{temp}°F = {result:.2f}K")

        elif choice == '6':
            result = (temp - 273.15) * 9/5 + 32
            print(f"{temp}K = {result:.2f}°F")
#here i am handling trhe edge case and if the user clicks any other number exceopt the given then it will come to else
    else:
        print("Invalid choice! Please select between 1-7.")
