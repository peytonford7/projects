import sys

title = "Pizza Menu".upper()
print(title.center(25, "-"))

print("1. Slice".ljust(18, ".") + "$3".rjust(5))
print("2. Garlic Bread".ljust(18, ".") + "$2".rjust(5))
print("3. Soda".ljust(18, ".") + "$1".rjust(5))

order_input = input("\nPick something (1-3): ")

try:
    order = int(order_input)
except ValueError:
    sys.exit("Not a number! Please try again")

print("\n")

match order_input:
    case 1:
        print("Slice of pizza, $3\n")
    case 2:
        print("Garlic bread, $2\n")
    case 3:
        print("Soda, $1\n")
    case _:
        sys.exit("That’s not on the menu. Try again.\n")
