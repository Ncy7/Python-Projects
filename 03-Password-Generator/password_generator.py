# 03-Password-Generator/password_generator.py
import random
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a secure password based on user preferences."""
    # Build the character pool
    pool = ""
    if use_lower:   pool += string.ascii_lowercase
    if use_upper:   pool += string.ascii_uppercase
    if use_digits:  pool += string.digits
    if use_symbols: pool += string.punctuation

    if not pool:
        return "Error: No character types selected!"

    # Generate password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

def main():
    print("🔐 Secure Password Generator 🔐\n")
    
    while True:
        try:
            length = int(input("Password length (8-128): "))
            if length < 8:
                print("Minimum length is 8!\n")
                continue
        except ValueError:
            print("Please enter a number!\n")
            continue

        # Simple test using all character types
        password = generate_password(
            length=length,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=True
        )
        
        print(f"\nGenerated Password:\n{password}\n")
        
        again = input("Generate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Stay safe! 🔒")
            break

if __name__ == "__main__":
    main()