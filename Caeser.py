text = input("Enter Text")
shift = int(input("Enter key"))
result = ""

for character in text:
    if character.isalpha():
        start = ord('A') if character.isupper() else ord('a')
        new_character = chr((ord(character) - start + shift) % 26 + start)
        result += new_character
    else:
        result += character

print("BY Caesar Cipher:",result)

text = result
shift = 3
result = ""
text = result
shift = 3
result = ""

for character in text:
    if character.isalpha():
        start = ord('A') if character.isupper() else ord('a')
        # Subtract the shift to reverse the encryption
        new_character = chr((ord(character) - start - shift) % 26 + start)
        result += new_character
    else:
        result += character

print(result) 
