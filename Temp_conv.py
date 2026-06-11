def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def time_travel_converter():
    print("=== TEMPORAL TEMPERATURE CONVERTER ===")
    print("1. Convert Celsius (°C) to Fahrenheit (°F)")
    print("2. Convert Fahrenheit (°F) to Celsius (°C)")
    
    # Get the user's choice of conversion
    choice = input("Select conversion type (1 or 2): ").strip()
    
    if choice == '1':
        # Celsius to Fahrenheit
        try:
            c_temp = float(input("Enter temperature in Celsius: "))
            f_result = celsius_to_fahrenheit(c_temp)
            print(f"🎒 Temporal Log: {c_temp}°C is equal to {f_result:.2f}°F")
        except ValueError:
            print("🚨 Error: Please enter a valid numerical temperature!")
            
    elif choice == '2':
        # Fahrenheit to Celsius
        try:
            f_temp = float(input("Enter temperature in Fahrenheit: "))
            c_result = fahrenheit_to_celsius(f_temp)
            print(f"🎒 Temporal Log: {f_temp}°F is equal to {c_result:.2f}°C")
        except ValueError:
            print("🚨 Error: Please enter a valid numerical temperature!")
            
    else:
        print("🛑 Error: Invalid choice. The time machine doesn't understand that scale!")

# Fire up the converter
if __name__ == "__main__":
    time_travel_converter()