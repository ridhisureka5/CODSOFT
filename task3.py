import random
import string
# function declaration
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    if not any([use_uppercase, use_lowercase, use_digits, use_special_chars]):
        print("At least one character type must be selected.")
        return None
     # adding value to the string characters for the function
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
# use of random to input random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
# passing the values to the above function
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    if password:
        print(f"Generated Password: {password}")
# calling the intial function name 
if __name__ == "__main__":
    main()
