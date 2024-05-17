from Crypto.Random import get_random_bytes


def store(password: str):
    salt = get_random_bytes(16)
