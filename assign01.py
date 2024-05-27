def caeser_encryption(Str, n):
    encry = ""

    for ch in Str:
        encry += (chr(ord(ch) + n))
    return encry


def caeser_decryption(Str, n):
    decry = ""

    for ch in Str:
        decry += (chr(ord(ch) - n))
    return decry


Str = input("Enter the String: ")
n = int(input("Enter the increment count:"))

Str = caeser_encryption(Str, n)
print("After Encryption String is:", Str)

Str = caeser_decryption(Str, n)
print("After Decryption string is:", Str)