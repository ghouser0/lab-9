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

def decode(password):
    decoded_pass = ""
    for bit in password:
        decoded_bit = str(int(bit) - 3)
        decoded_pass += decoded_bit
    return decoded_pass


def main():
    original_pass = ""

    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            original_pass = password
            print("Your password has been encoded and stored!")

        elif option == 2:
            if original_pass:
                decoded_pass = decode(encoded_pass)
                print(f"The encoded password is {encoded_pass}, and the original password is {original_pass}.")
            else:
                print("Please encode a password first.")

        elif option == 3:
            break

if __name__ == "__main__":
    main()
