
english_freq = {
    "A": 8.17, "B": 1.49, "C": 2.78,
    "D": 4.25, "E": 12.70, "F": 2.23,
    "G": 2.02, "H": 6.09, "I": 6.97,
    "J": 0.15, "K": 0.77, "L": 4.03,
    "M": 2.41, "N": 6.75, "O": 7.51,
    "P": 1.93, "Q": 0.10, "R": 5.99,
    "S": 6.33, "T": 9.06, "U": 2.76,
    "V": 0.98, "W": 2.36, "X": 0.15,
    "Y": 1.97, "Z": 0.07
}

def encrypt(message , key):
    encrypted_message = ""
    for letter in message:
        if letter.isalpha() and letter.isascii():
            letter = letter.upper()
            number = ord(letter) - ord("A")
            encrypted_number = (number + key) % 26
            encrypted_letter = chr(encrypted_number + ord("A"))

            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    return(encrypted_message)

def decrypt(message, key):
    decrypted_message = ""
    for letter in message:
        if letter.isalpha() and letter.isascii():
            letter = letter.upper()
            number = ord(letter) - ord("A")
            decrypted_number = (number - key) % 26
            decrypted_letter = chr(decrypted_number + ord("A"))
        
            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter
    return(decrypted_message)


def get_key():
    while True:
        try:
            key = int(input("Enter key: "))
            return key

        except ValueError:
            print("Invalid key. Please enter a whole number.")



def brute_force(message):
    results = []

    for key in range(26):
        decrypted = decrypt(message, key)

        results.append({
            "key": key,
            "message": decrypted
        })

    return results


def letter_frequency(message):
    message = message.upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = sum(message.count(letter) for letter in alphabet)

    if total == 0:
        return {}

    frequencies = {}

    for letter in alphabet:
        count = message.count(letter)
        percentage = (count / total) * 100

        frequencies[letter] = percentage

    return frequencies


def chi_square(message):
    message = message.upper()

    total = sum(message.count(letter) for letter in english_freq)

    if total == 0:
        return float("inf")

    score = 0

    for letter in english_freq:
        observed = message.count(letter)
        expected = (english_freq[letter] / 100) * total

        score += ((observed - expected) ** 2) / expected

    return score



def auto_crack(message):
    results = []

    for key in range(26):
        decrypted = decrypt(message, key)
        score = chi_square(decrypted)

        results.append((score, key, decrypted))

    results.sort()

    best_score, best_key, best_message = results[0]

    return {
        "key": best_key,
        "message": best_message,
        "score": best_score
    }












