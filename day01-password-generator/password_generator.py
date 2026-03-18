import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Password length (default 12): ") or 12)
    except ValueError:
        length = 12

    symbols = input("Include symbols? (y/n, default y): ").strip().lower()
    use_symbols = symbols != 'n'

    how_many = int(input("How many passwords? (default 1): ") or 1)

    print("\nGenerated passwords:")
    for i in range(how_many):
        print(f"  {i+1}. {generate_password(length, use_symbols)}")

if __name__ == "__main__":
    main()