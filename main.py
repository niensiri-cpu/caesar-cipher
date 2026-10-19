from caesar import encrypt, decrypt, brute_force, auto_crack, get_key


def main():
    while True:
        print("\n=== Caesar Cipher ===")
        print("e - Encrypt")
        print("d - Decrypt")
        print("b - Brute force")
        print("a - Auto crack")
        print("q - Quit")

        choice = input("Choose an option: ").strip().lower()
    
        if choice == "q":
            print("Goodbye!")
            break

        elif choice == "e":
            message = input("Enter message to encrypt: ")
            key = get_key()

            result = encrypt(message, key)
            print("Encrypted message:", result)

        elif choice == "d":
            message = input("Enter message to decrypt: ")
            key = get_key()
            result = decrypt(message, key)
            print("Decrypted message:", result)

    
        elif choice == "b":
            message = input("Enter encrypted message: ")

            results = brute_force(message)

            for result in results:
                print(
                    "Key:", result["key"],
                    "| Message:", result["message"]
                )
        
        elif choice == "a":
            message = input("Enter encrypted message: ")

            result = auto_crack(message)

            print("Most likely key:", result["key"])
            print("Decrypted message:", result["message"])
            print("Chi-square score:", round(result["score"], 2))


        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

