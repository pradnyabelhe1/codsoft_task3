import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator\n")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a valid length greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for the length.")
            continue

        generated_password = generate_password(length)
        print(f"\nGenerated Password: {generated_password}")

        reset_option = input("\nDo you want to reset the password? (yes/no): ").lower()
        if reset_option != 'yes':
            break

if __name__ == "__main__":
    password_generator()
