# shopping_list_manager.py
def display_menu():
    # Correct format for printing the "Shopping List Manager" heading
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View LIst")
    print("4. Exit")
    def main():
        shopping_list = []
        while True:
            display_menu()
            choice = input("Enter your choice:" )
           if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: "). strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
           elif choice == '2':
               # Prompt for and remove an item
               item = input("Enter the item to remove: ").strip()
               if item in shopping_list:
                   shopping_list.remove(item)
                   print(f"'item' has been removed from the shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")
           elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrentt shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
              else:
                print("\nYour shopping list is currently empty.")
           elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")
if__name__ == "__main__":
main()                                
