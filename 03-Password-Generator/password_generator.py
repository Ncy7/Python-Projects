# 03-Password-Generator/password_generator.py
import random
import string
import pyperclip  # ← New! Copies to clipboard

def get_char_pool(include_lower, include_upper, include_digits, include_symbols):
    pool = ""
    guaranteed = []
    
    if include_lower:
        pool += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if include_upper:
        pool += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if include_digits:
        pool += string.digits
        guaranteed.append(random.choice(string.digits))
    if include_symbols:
        pool += string.punctuation
        guaranteed.append(random.choice(string.punctuation))
    
    return pool, guaranteed

def generate_password(length, include_lower, include_upper, include_digits, include_symbols):
    if length < 4:
        return "Error: length too short!"
    
    pool, guaranteed = get_char_pool(include_lower, include_upper, include_digits, include_symbols)
    if not pool:
        return "Error: select at least one character type!"
    
    # Fill the rest with random chars
    remaining = length - len(guaranteed)
    password_chars = guaranteed + [random.choice(pool) for _ in range(remaining)]
    random.shuffle(password_chars)  # ← Makes it truly random order
    
    return ''.join(password_chars)

def main():
    print("🔐 Secure Password Generator Pro 🔐\n")
    
    while True:
        try:
            length = int(input("Password length (8-128): "))
            if length < 8:
                print("Too short! Minimum 8.\n")
                continue
        except ValueError:
            print("Please enter a number!\n")
            continue

        print("\nInclude:")
        lower = input("  Lowercase letters? (y/n): ").strip().lower() == 'y'
        upper = input("  Uppercase letters? (y/n): ").strip().lower() == 'y'
        digits = input("  Numbers? (y/n): ").strip().lower() == 'y'
        symbols = input("  Symbols (!@#$ etc)? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, lower, upper, digits, symbols)
        print(f"\n{password}\n")
        
        # Copy to clipboard!
        pyperclip.copy(password)
        print("✅ Copied to clipboard!\n")

        again = input("Generate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Stay safe out there! 🔒")
            break

if __name__ == "__main__":
    main()