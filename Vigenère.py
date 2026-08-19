message = input("enter text")
key = int(input("KEY"))

message = message.upper()
key = key.upper()

ciphertext = ""
key_index = 0

for let in message:
    if let.isalpha():
        p_num = ord(let) - 65
        k_num = ord(key[key_index % len(key)]) - 65
        
        c_num = (p_num + k_num) % 26
        
        ciphertext += chr(c_num + 65)
        key_index += 1
    else:
        ciphertext += let
print("BY Vigenère Cipher:", ciphertext)

ciphertext= "SRQK WSWQCB XYVILD"
key = "KEY"

ciphertext = ciphertext.upper()
key = key.upper()

plaintext = ""
key_index = 0

for let in ciphertext:
    if let.isalpha():
        
        c_num = ord(let) - 65
        k_num = ord(key[key_index % len(key)]) - 65
        
        p_num = (c_num - k_num) % 26
        
        plaintext += chr(p_num + 65)
        key_index += 1
    else:
        plaintext += let

print("Decrypted Plaintext:", plaintext) 

