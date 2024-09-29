# Import the necessary components from the datetime module
from datetime import datetime, timedelta
# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    # Format the date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date   # Return the current date to use in the second part
# Part 2: Calculate a future Date
def calculate_future_date(current_date):
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date as YYYY-MM-DD
    # formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date 
    # Main function to call the two parts
    def main():
        # Part 1: Display the current date and time
        current_date = display_current_datetime()
        # Part 2: Calculate and display the future date
        calculate_future_date(current_date)
    if __name__ == "__main__":
        main()        