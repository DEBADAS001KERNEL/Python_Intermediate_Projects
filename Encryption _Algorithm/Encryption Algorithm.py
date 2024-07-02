# Lists of uppercase letters and their corresponding special characters
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.']

def encrypt_message(input_string):
    """Encrypts a message by converting uppercase letters to special characters."""
    uppercase_string = input_string.upper()
    char_list = list(uppercase_string)
    index_list = [uppercase.index(char) for char in char_list]
    special_char_list = [special[index] for index in index_list]
    return special_char_list

def decrypt_message(special_char_list):
    """Decrypts a message by converting special characters back to uppercase letters."""
    try:
        char_to_uppercase = {special[i]: uppercase[i] for i in range(len(special))}
        original_message = ''.join(char_to_uppercase[char] for char in special_char_list)
        return original_message
    except KeyError as e:
        return f"Error: Invalid character '{e}' found in the input. Please check the input and try again."

# Main program loop
while True:
    # Prompt user to choose between encryption, decryption, or exit
    user = input("PRESS 1 FOR ENCRYPT THE MESSAGE, PRESS 2 FOR DECODE THE MESSAGE, OR PRESS 3 TO EXIT: ")

    if user == "1":
        # Encryption process
        input_string = input("PLEASE ENTER YOUR MESSAGE WITH ONLY UPPERCASE LETTERS: ")
        encrypted_message = encrypt_message(input_string)
        print("Encrypted message:", encrypted_message)

    elif user == "2":
        # Decryption process
        input_special_chars = input("ENTER SPECIAL CHARACTERS TO DECRYPT (separated by spaces): ").split()
        decrypted_message = decrypt_message(input_special_chars)
        print("Decrypted message:", decrypted_message)

    elif user == "3":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid input. Please enter '1', '2', or '3'.")