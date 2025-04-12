def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def encode_to_string(text):
    encoded_str = ""
    for i, char in enumerate(text):
        fib = fibonacci(i + 1)
        encoded_value = ord(char) + fib
        hex_repr = f"{encoded_value:04x}"  # 4-digit hex
        encoded_str += hex_repr
    return encoded_str

def decode_from_string(encoded_str):
    decoded = ""
    for i in range(0, len(encoded_str), 4):
        hex_chunk = encoded_str[i:i+4]
        encoded_value = int(hex_chunk, 16)
        fib = fibonacci(i // 4 + 1)
        original_char = chr(encoded_value - fib)
        decoded += original_char
    return decoded

# Example
original = "Hello, GPT!"
encoded = encode_to_string(original)
decoded = decode_from_string(encoded)

print("Original:", original)
print("Encoded String:", encoded)
print("Decoded:", decoded)
