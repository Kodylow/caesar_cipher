
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    #assume only uppercase letters, can just use ord("A")
    for letter in plaintext:
        ciphertext += chr((ord(letter) - ord("A") + key) % 26 + ord("A"))
    print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    #assume only uppercase letters, can just use ord("A")
    for letter in ciphertext:
        plaintext += chr((ord(letter) - ord("A") - key) % 26 + ord("A"))
    print(plaintext)
    return plaintext


