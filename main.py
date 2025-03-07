from models.circle import Circle

def main():
    print("Welcome to the Circle Calculator!")
    
    # Ask user for the circle's diameter
    diameter = float(input("Enter the circle's diameter: "))
    my_circle = Circle(diameter)

    while True:
        print("\nChoose a calculation:")
        print("1. Radius")
        print("2. Diameter")
        print("3. Circumference")
        print("4. Area")
        print("5. Central Angle (requires additional input)")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print(f"Radius: {my_circle.radius}")
        elif choice == "2":
            print(f"Diameter: {my_circle.diameter()}")
        elif choice == "3":
            print(f"Circumference: {my_circle.circumference()}")
        elif choice == "4":
            print(f"Area: {my_circle.area()}")
        elif choice == "5":
            angle = float(input("Enter the central angle in degrees: "))
            print(f"Central Angle (in radians): {my_circle.central_angle(angle)}")
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()