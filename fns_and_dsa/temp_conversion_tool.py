# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Correct conversion factor from F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Correct conversion factor from C to F
OFFSET = 32   # Constant used in both conversions
# Function to convert fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    # Using the required formula (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
# Function to convert celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    # Using the required formula (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
# Main function for user interaction
def main():
    try:
        # Get the temperature input from the user
        temperature = float(input("Enter the temperature to convert: "))
        # Get the unit (C for Celsius, F for Fahrenheit)
        unit =input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        # Perform the conversion based on the user's input
        if unit == 'C':
            # Convert Celsius to Fahrenheit 
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp + convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ =="__main__":
    main()                               