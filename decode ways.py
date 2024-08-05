encoded_message = "dwwdfn"
alphabet = "abcdefghijklmnopqrstuvwxyz"
decoded_messages = []
for shift in range(26):
    decoded_message = ""
    for char in encoded_message:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % 26
            decoded_message += alphabet[index]
        else:
            decoded_message += char  
    decoded_messages.append(decoded_message)
for i, message in enumerate(decoded_messages):
    print(f"Shift {i}: {message}")
