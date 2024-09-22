# pattern_drawing.py
# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Initialize the row counter for the while loop
row = 0
# Use a while loop to control the number of rows
while row < size:
    # Use a for loop to print each row of asterisks
    for col in range(size):
        print("*", end="")
        # Move to the next line after printing one row of asterisks
        print()
        # Increment the row counter
        row += 1
        