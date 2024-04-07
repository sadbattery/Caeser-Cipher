```python

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                if mode == '1':
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                elif mode == '2':
                    result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                # Shift lowercase letters
                if mode == '1':
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
                elif mode == '2':
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result
mode=0;
# Ask user for mode (encrypt or decrypt)
mode = input("Enter 1 for 'encrypt' or 2 for 'decrypt': ")

# Ask user to input message and shift value
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if mode == "1":
    encrypted_text = caesar_cipher(text, shift, mode)
    print("Encrypted:", encrypted_text)
elif mode == "2":
    decrypted_text = caesar_cipher(text, shift, mode)
    print("Decrypted:", decrypted_text)
else:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")


```
