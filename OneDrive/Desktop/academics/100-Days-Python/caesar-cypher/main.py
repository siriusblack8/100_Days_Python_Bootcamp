# encode or decode
# encode - add the shift number to the position of the alphabet, replace the current alphabet with alphabet in the obtained position
# if after adding position>26 -> subtract 26 from it
# decode - subtract the shift number from the position of the alphabet, replace the current alphabet with alphabet in the obtained position
# if after subtracting position is<0 -> add 26 to it

def encode_caesar_cypher(a,b):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(a)):
        if a[i]==" ":
            continue
        else:
            pos = alphabet.index(a[i])
            a[i] = alphabet[(pos+b)%26]
    return(''.join(a))
    
def decode_caesar_cypher(a,b):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(a)):
        if a[i]== " ":
            continue
        else:
            pos = alphabet.index(a[i])
            a[i] = alphabet[((pos-b)+26)%26]
    return(''.join(a))

def caesar_cypher():
    print("Welcome to Caesar Cipher!")
    while True:
        encode_or_decode = (str(input("Do you want to encode or decode the word? (type 'encode' or 'decode'):"))).lower()
        word = list((input("Enter the word: ")).lower())
        shift_num = int(input("Enter shift number: "))
        
        if encode_or_decode == "encode":
            print(f"The encoded word is: {encode_caesar_cypher(word, shift_num)}")
        else:
            print(f"The decoded word is: {decode_caesar_cypher(word, shift_num)}")
        
        cont = (str(input("Do you want to continue or exit?(Type yes to continue and no to exit):"))).lower()
        if cont != "yes":
            print("Thank you!")
    

caesar_cypher()

    