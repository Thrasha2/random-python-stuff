def encode(message,shift):
    newword = ""
    for letter in message:
        number = ord(letter)
        number = number + shift
        newLetter = chr(number)
        newword += newLetter
    return newword
def decode(message,shift):
    newword = ""
    for letter in message:
        number = ord(letter)-shift
        newletter = chr(number)
        newword += newletter
        return newword
goagain = 1
while goagain == 1:
    message = input("Enter a message: ")
    shift = int(input("Enter a shift: "))
    encodeordecode = input("would you like to encode(1) or decode(2): ")
    match encodeordecode:
        case "1":
            print(encode(message,shift))
        case "2":
            print(decode(message,shift))
    goagain = input("would you like to go again? (1 yes anything else for no): ")