def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

print("🌡️ Temperature Converter")
print("1. Celsius to Fahrenheit & Kelvin")
print("2. Fahrenheit to Celsius & Kelvin")
print("3. Kelvin to Celsius & Fahrenheit")

choice = input("Enter your choice (1/2/3): ")

try:
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
        print(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f}K")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {c:.2f}°C")
        print(f"{fahrenheit}°F = {celsius_to_kelvin(c):.2f}K")
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        c = kelvin_to_celsius(kelvin)
        print(f"{kelvin}K = {c:.2f}°C")
        print(f"{kelvin}K = {celsius_to_fahrenheit(c):.2f}°F")
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
except ValueError:
    print("❌ Please enter a valid numeric value.")
