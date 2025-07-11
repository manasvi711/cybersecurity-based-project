def encrypt_decrypt_char(char, shift, mode):
    """
    Encrypts or decrypts a single character using the Caesar Cipher logic.
    Handles uppercase, lowercase letters, and wraps around the alphabet.
    Non-alphabetic characters are returned unchanged.
    """
    if 'a' <= char <= 'z':  # Process lowercase letters
        start = ord('a')
        if mode == "encrypt":
            shifted_char_code = (ord(char) - start + shift) % 26 + start
        else:  # mode == "decrypt"
            shifted_char_code = (ord(char) - start - shift + 26) % 26 + start
        return chr(shifted_char_code)

    elif 'A' <= char <= 'Z':  # Process uppercase letters
        start = ord('A')
        if mode == "encrypt":
            shifted_char_code = (ord(char) - start + shift) % 26 + start
        else:  # mode == "decrypt"
            shifted_char_code = (ord(char) - start - shift + 26) % 26 + start
        return chr(shifted_char_code)

    else:
        return char  # Return non-alphabetic characters as they are

def caesar_cipher_message(text, shift, mode):
    """
    Applies the Caesar Cipher to an entire message.
    """
    result_message = ""
    for char in text:
        processed_char = encrypt_decrypt_char(char, shift, mode)
        result_message += processed_char
    return result_message

def main():
    """
    Main function to run the Caesar Cipher program with user interaction.
    """
    while True:
        print("\n--- Caesar Cipher Program ---")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip() # .strip() removes whitespace

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (e.g., 3 for 'A' -> 'D'): "))
            except ValueError:
                print("Invalid shift value. Please enter a whole number.")
                continue # Go back to the start of the loop

            encrypted_text = caesar_cipher_message(message, shift, "encrypt")
            print(f"Encrypted Message: {encrypted_text}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (e.g., 3 if it was encrypted with 3): "))
            except ValueError:
                print("Invalid shift value. Please enter a whole number.")
                continue # Go back to the start of the loop

            decrypted_text = caesar_cipher_message(message, shift, "decrypt")
            print(f"Decrypted Message: {decrypted_text}")

        elif choice == '3':
            print("Exiting Caesar Cipher program. Goodbye!")
            break # Exit the while loop

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Entry point of the script
if __name__ == "__main__":
    main()