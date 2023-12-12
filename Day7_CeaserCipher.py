def encode(text, shift):
    encodedText = ""
    for value in range(0, len(text)):
        index_Item = alphabet.index(text[value])
        shiftIndex = index_Item + shift
        if shiftIndex > len(alphabet):
            shiftIndex = shiftIndex - (len(alphabet) - index_Item)
        encodedText += alphabet[shiftIndex]
    print(f"Encoded Text is: {encodedText}")


def decode(text, shift):
    decodedText = ""
    for value in range(0, len(text)):
        index_Item = alphabet.index(text[value])
        shiftIndex = index_Item - shift
        decodedText += alphabet[shiftIndex]
    print(f"Decoded Text: {decodedText}")


do = True
while input("Do you want to continue: Y or N: ") != "N":
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode(text, shift)
    else:
        decode(text, shift)
