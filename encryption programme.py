import random
import string

# -----------------------------
# SETUP
# -----------------------------
chars = list(" " + string.punctuation + string.digits + string.ascii_letters)

key = chars.copy()
random.shuffle(key)

# -----------------------------
# FUNCTIONS
# -----------------------------

def encrypt():
    plain_text = input("\n🔐 Enter your message to encrypt:\n> ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print("\n✅ Encryption Successful!")
    print("📄 Original Text :", plain_text)
    print("🔒 Encrypted Text:", cipher_text)


def decrypt():
    cipher_text = input("\n🔓 Enter your encrypted message:\n> ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print("\n✅ Decryption Successful!")
    print("🔒 Cipher Text   :", cipher_text)
    print("📄 Original Text :", plain_text)


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("🔐 Welcome to the Python Encryption Tool 🔐")
print("------------------------------------------")

while True:
    print("\nChoose an option:")
    print("1️⃣ Encrypt a message")
    print("2️⃣ Decrypt a message")
    print("3️⃣ Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        print("\n👋 Exiting program. Goodbye!")
        break
    else:
        print("\n❌ Invalid choice. Please try again.")
