import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a valid positive integer for the length.")
    return length

def main():
    length = get_password_length()
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
