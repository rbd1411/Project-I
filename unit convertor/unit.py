def convert_temperature():
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        scale_from = input("Enter scale to convert from (C, F, K): ").upper()
        if scale_from in ["C", "F", "K"]:
            break
        else:
            print("Invalid input. Please enter C, F, or K.")

    while True:
        scale_to = input("Enter scale to convert to (C, F, K): ").upper()
        if scale_to in ["C", "F", "K"]:
            break
        else:
            print("Invalid input. Please enter C, F, or K.")

    if scale_from == "C":
        if scale_to == "F":
            result = temperature * 1.8 + 32
        elif scale_to == "K":
            result = temperature + 273.15
        else:
            result = temperature
    elif scale_from == "F":
        if scale_to == "C":
            result = (temperature - 32) / 1.8
        elif scale_to == "K":
            result = (temperature + 459.67) * 5/9
        else:
            result = temperature
    else:
        if scale_to == "C":
            result = temperature - 273.15
        elif scale_to == "F":
            result = temperature * 9/5 - 459.67
        else:
            result = temperature

    print(f"{temperature} {scale_from} is {result:.2f} {scale_to}.")

def convert_length():
    while True:
        try:
            length = float(input("Enter length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        unit_from = input("Enter unit to convert from (m, km, mi): ").lower()
        if unit_from in ["m", "km", "mi"]:
            break
        else:
            print("Invalid input. Please enter m, km, or mi.")

    while True:
        unit_to = input("Enter unit to convert to (m, km, mi): ").lower()
        if unit_to in ["m", "km", "mi"]:
            break
        else:
            print("Invalid input. Please enter m, km, or mi.")

    if unit_from == "m":
        if unit_to == "km":
            result = length / 1000
        elif unit_to == "mi":
            result = length / 1609.34
        else:
            result = length
    elif unit_from == "km":
        if unit_to == "m":
            result = length * 1000
        elif unit_to == "mi":
            result = length / 1.60934
        else:
            result = length
    else:
        if unit_to == "m":
            result = length * 1609.34
        elif unit_to == "km":
            result = length * 1.60934
        else:
            result = length

    print(f"{length} {unit_from} is {result:.2f} {unit_to}.")

def main():
    while True:
        print("\n1. Convert temperature")
        print("2. Convert length")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            convert_temperature()
        elif choice == "2":
           convert_length()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
