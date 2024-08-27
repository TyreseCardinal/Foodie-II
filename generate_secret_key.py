import secrets

def generate_secret_key(length=32):
    """Generate a cryptographically secure secret key."""
    return secrets.token_hex(length)

if __name__ == '__main__':
    secret_key = generate_secret_key()
    print(f"Your new secret key is: {secret_key}")
