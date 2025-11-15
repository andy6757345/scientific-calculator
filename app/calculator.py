# app/calculator.py
import math

def menu():
    print("\nScientific Calculator Menu:")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln x)")
    print("4. Power (x^a)")
    print("5. Exit")

def square_root():
    x = float(input("Enter number: "))
    print(f"√{x} = {math.sqrt(x)}")

def factorial():
    x = int(input("Enter integer: "))
    print(f"{x}! = {math.factorial(x)}")

def natural_log():
    x = float(input("Enter number: "))
    print(f"ln({x}) = {math.log(x)}")

def power():
    x = float(input("Enter base: "))
    b = float(input("Enter exponent: "))
    print(f"{x}^{a} = {math.pow(x, b)}")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            square_root()
        elif choice == '2':
            factorial()
        elif choice == '3':
            natural_log()
        elif choice == '4':
            power()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
