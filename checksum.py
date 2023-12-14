import hashlib

def generate_checksum(token, payload, signature):
    """
    Generate a checksum by hashing a UTF-16 Little Endian encoded string.
    The string is formed by concatenating slices of payload and signature with a token.
    The hash is SHA1, and a portion of the hash is converted to an uppercase hexadecimal string.

    Parameters:
    token (str): A string token.
    payload (str): Base64 encoded payload.
    signature (str): Base64 encoded signature.

    Returns:
    str: The generated checksum.
    """
    try:
        # Build plaintext
        plaintext = payload[10:20] + token + signature[2:10]

        # Convert to UTF-16 LE and hash using SHA1
        hash_digest = hashlib.sha1(plaintext.encode('utf-16le')).digest()

        # Select specific bytes, convert to hex and uppercase
        checksum = hash_digest[2:10].hex().upper()

        return checksum
    except Exception as e:
        # Handle potential errors
        print(f"An error occurred: {e}")
        return None

# Example usage
token = "Don'tMessWithMMS"
payload = ""   # base64 encoded payload
signature = "" # base64 encoded signature

# Generate and print checksum
print(generate_checksum(token, payload, signature))