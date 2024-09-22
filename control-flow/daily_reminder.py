# daily_reminder.py
# Prompt user for the task description
task = input("Enter your task: ")
# Prompt user for the priority level
priority = input("Priority (high/medium/low): ").lower()
# Ask the user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Generate reminder based on priority using Match Case
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
        # Modify reminder if the task is time-sensitive
if time_bound == 'yes':
    reminder += " that requires immediate attension today!"
else:
    reminder += ". Consider completing it when you have free time"   
# Print the final reminder
 print(f"Reminder: {reminder}")
         