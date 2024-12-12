def encrypt(message):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + 1)
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr(ord(char) - 1)
        decrypted_message += decrypted_char
    return decrypted_message

str = "Hello, World!"

encrypted_str = encrypt(str)
print("加密后的字符：", encrypted_str)

decrypted_str = decrypt(encrypted_str)
print("解密后的字符：", decrypted_str)