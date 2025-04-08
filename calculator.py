def to_hex(x):
    return hex(int(x))

def from_hex(s):
    try:
        return int(s, 16)
    except ValueError:
        return "Invalid hexadecimal number"

def hex_calculator():
    print("Hex Calculator")
    print("1. Convert Decimal to Hex")
    print("2. Convert Hex to Decimal")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        num = input("Enter decimal number: ")
        try:
            dec = int(num)
            print(f"Hex: {to_hex(dec)}")
        except ValueError:
            print("Invalid decimal number")
    elif choice == '2':
        num = input("Enter hex number (e.g., 1a): ")
        result = from_hex(num)
        print(f"Decimal: {result}")
    else:
        print("Invalid choice")

def hex_mul():
    a = 0x46
    b = 0x31
    print(f"Result: {(a * b)}")
    return

hex_calculator()
hex_mul()

