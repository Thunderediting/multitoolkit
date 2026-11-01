
from toolkit import datetime
from toolkit import math
from toolkit import random
from toolkit import file
from toolkit import module

import uuid


def main_menu():

    while True:

        print("\n==============================")
        print("WELCOME TO MULTI-UTILITY TOOLKIT")
        print("==============================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifier")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime.menu()

        elif choice == "2":
            math.menu()

        elif choice == "3":
            random.menu()

        elif choice == "4":
            print("Generated UUID:", uuid.uuid4())

        elif choice == "5":
            file.menu()

        elif choice == "6":
            module.explore()

        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
