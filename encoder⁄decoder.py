import tkinter as tk

def encode(message,shift):
    newword = ""
    for letter in message:
        number = ord(letter)
        number = number + shift
        newLetter = chr(number)
        newword += newLetter
    return newword
def decode(message, shift):
    newword = ""
    for letter in message:
        number = ord(letter)
        number = number - shift
        newLetter = chr(number)
        newword += newLetter
    return newword

decodeOrEncode = "0"
while decodeOrEncode != "1" or  "2":
    print("---------------------------")
    message = input("input your message: ")
    shift = int(input("input the shift: "))
    print("---------------------------")
    decodeOrEncode = encode(message,shift)
    decodeOrEncode = input("would you like to encode(1) or decode(2) your message?")
    if decodeOrEncode == "1":
        encodedMessage = encode(message, shift)
        print("the encoded message is '" ,encodedMessage,"'")
        pass
    elif decodeOrEncode == "2":
        decodedMessage = decode(message, shift)
        print("the decoded message is '", decodedMessage, "'")
        pass

