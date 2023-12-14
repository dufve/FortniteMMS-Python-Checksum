# FortniteMMS-Python-Checksum

This script is designed to replicate the checksum computation used in Fortnite, which is crucial for accessing the game's matchmaking services.

### Input Variables

- `token`: A unique string token for each use case.
- `payload`: Your base64 encoded payload.
- `signature`: Your base64 encoded signature.

### Checksum Calculation Process

The checksum is calculated by following these steps:

1. **Concatenation**: The script forms a plaintext string by concatenating three parts: a subset of the payload (characters 10 to 20), the entire token, and a subset of the signature (characters 2 to 10).
2. **UTF-16 Encoding**: This plaintext string is then encoded in UTF-16 using Little Endian byte order.
3. **SHA1 Hashing**: The UTF-16 encoded data is hashed using the SHA1 algorithm to produce a 20-byte hash value.
4. **Hex Encoding and Upper Case Conversion**: From the SHA1 hash, bytes 2 to 10 are extracted and converted into a hexadecimal string. This string is then transformed into uppercase letters to standardize the format.
5. **Output**: The resulting uppercase hexadecimal string is the checksum.

### Usage

To use the script, define the `token`, `payload`, and `signature` variables with the appropriate values. Then, call the `generate_checksum` function with these variables as arguments. The function will return the calculated checksum based on the provided inputs.

```python
# Example usage
token = "YourToken"
payload = "YourBase64EncodedPayload"
signature = "YourBase64EncodedSignature"

# Generate and print checksum
print(generate_checksum(token, payload, signature))

## Disclaimer

This software is provided for educational and scientific purposes only. The author or contributors are not responsible for any possible harm caused by misuse of this software. It is provided as-is without any express or implied warranty. In no event will the author be held liable for any damages arising from the use of this software. Any modification or use of the software for purposes other than educational and scientific purposes is at the user's own risk and discretion.