import string
import sys

def decrypt(encrypted_text, shift_value):
    """
    Decrypt the given encrypted text using the given shift value
    """
    encrypted_text = encrypted_text.lower()
    
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    # maketrans maps alphabets from respective index eg
    table = str.maketrans(alphabet, shifted_alphabet)
    return encrypted_text.translate(table)

def bruteforce_decrypt(encrypted_text):
    """
    Try all possible shift values (1-25) and return the decryption that
    most closely resembles an English text.
    """
    decrypted_texts = []
    for shift_value in range(1, 26, 2): # for 3 shift = 5, for 2 shift = 15, else 12 
        decrypted_text = decrypt(encrypted_text, shift_value)
        decrypted_texts.append((shift_value,decrypted_text))
    return decrypted_texts

# checks if the texts contain any numeric value.
def contains_number(text):
    for char in text:
        if char.isdigit():
            return True
    return False

def main(filename):
    try:
        with open(filename, "r") as file:
            encrypted_text = file.read()
            if(contains_number(encrypted_text)): # calling the containsNumber and encrypted_text as argument.
                print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")
                return
            
            decrypted_texts = bruteforce_decrypt(encrypted_text)# calling bruteforce_decrypt with encrypted_text as an argument.
            for shift_value, decrypted_text in decrypted_texts:
                print(f" shift:{shift_value} decryption: {decrypted_text}")
                print()
    except:
        print("Cannot open {}. Sorry about that.".format(filename))

#allows to execute code when file run as script.
if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
