def fibonacci(n):
    """Return the n-th Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def key_to_offset(secret_key):
    """Convert secret key to a numeric offset."""
    return sum(ord(c) for c in secret_key) % 50  # Keep offset reasonable

def encode_with_key(text, key):
    offset = key_to_offset(key)
    encoded_str = ""
    for i, char in enumerate(text):
        fib = fibonacci(i + 1 + offset)
        encoded_value = ord(char) + fib
        hex_repr = f"{encoded_value:04x}"
        encoded_str += hex_repr
    return encoded_str

def decode_with_key(encoded_str, key):
    offset = key_to_offset(key)
    decoded = ""
    for i in range(0, len(encoded_str), 4):
        hex_chunk = encoded_str[i:i+4]
        encoded_value = int(hex_chunk, 16)
        fib = fibonacci(i // 4 + 1 + offset)
        original_char = chr(encoded_value - fib)
        decoded += original_char
    return decoded

# 🔐 Example usage
text = "SecretMessage123"
key = "MySuperSecretKey"

encoded = encode_with_key(text, key)
decoded = decode_with_key(encoded, key)

print("Original:", text)
print("Encoded:", encoded)
print("Decoded:", decoded)
