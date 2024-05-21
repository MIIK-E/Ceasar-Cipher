def caesar_encrypt(text, shift):
    """Encrypt the text using Caesar cipher with the specified shift."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    """Decrypt the text using Caesar cipher with the specified shift."""
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def get_user_choice():
    """Get the user's choice to either encrypt or decrypt a message."""
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            return choice
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

def get_shift_value():
    """Get the shift value for the Caesar cipher."""
    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def main():
    print("Welcome to the Caesar Cipher Application!")
    choice = get_user_choice()
    text = input("Enter the message: ")
    shift = get_shift_value()

    if choice == 'e':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
