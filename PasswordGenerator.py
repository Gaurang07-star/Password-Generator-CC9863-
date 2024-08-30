import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols
    
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
         
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
