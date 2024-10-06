def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift - shift_base) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters are unchanged
    return decrypted_text

def brute_force_caesar_decrypt(ciphertext):
    for shift in range(1, 26):  # Try all shifts from 1 to 25
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    # Take input from the user
    ciphertext = input("Enter the ciphertext to decrypt: ")
    print("Brute-force Decryption Results:")
    brute_force_caesar_decrypt(ciphertext)
