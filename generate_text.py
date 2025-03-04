import random
import string

def generate_random_text(length=6):
    """Generate a random string of letters with the given length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

if __name__ == "__main__":
    print(generate_random_text())