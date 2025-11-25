"""Simple example using the cryptography library."""

from cryptography.fernet import Fernet


def main():
    # Generate a key
    key = Fernet.generate_key()
    print(f"Generated key: {key.decode()}")

    # Create a Fernet instance
    cipher = Fernet(key)

    # Encrypt a message
    message = b"Hello, World!"
    encrypted = cipher.encrypt(message)
    print(f"Encrypted message: {encrypted.decode()}")

    # Decrypt the message
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted message: {decrypted.decode()}")


if __name__ == "__main__":
    main()
