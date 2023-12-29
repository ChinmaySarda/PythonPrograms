message = input("Enter a message to encode or decode or just hit [ENTER] to stop: ")
while message != "":
    message = message.upper()
    output = ""
    for letter in message:
        if letter.isupper():
            value = ord(letter) + 13
            letter = chr(value)
            if not letter.isupper():
                    value -= 26
            letter = chr(value)
        output += letter
    print("Output message: ", output)
    message = input("Enter another message to encode or decode or just hit [ENTER] to stop: ")
print("Okay, we're done")
