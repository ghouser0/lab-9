# Gabriela Houser

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    encoded_pass = ""
    for bit in password:
        encoded_bit = str(int(bit) + 3)
        encoded_pass += encoded_bit
    return encoded_pass


def main():
    menu()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_pass = encode(password)
        print("Your password has been encoded and stored!")

    elif option == 2:
        pass

    elif option == 3:
        quit



if __name__ == "__main__":
    main()