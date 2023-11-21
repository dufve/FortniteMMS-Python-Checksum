#     FortniteMMS-Python-Checksum

This script is crafted to produce a checksum using specific inputs: a token, payload, and signature. Its checksum computation mirrors that used in Fortnite, playing a key role in accessing the game's matchmaking services.

### Input Variables

    Token: A string token, unique to each use case.
    Payload: A base64 encoded payload, typically representing the data to be secured.
    Signature: A base64 encoded signature, usually a unique identifier or key.

### Checksum Calculation Process

- The checksum is calculated by following these steps
  - 1. Concatenation: The script forms a plaintext string by concatenating three parts: a subset of the payload (characters 10 to 20), the entire token, and a subset of the signature (characters 2 to 10).
  - 2. UTF-16 Encoding: This plaintext string is then encoded in UTF-16 using Little Endian byte order.
  - 3. SHA1 Hashing: The UTF-16 encoded data is hashed using the SHA1 algorithm. SHA1 is a widely used cryptographic hash function that produces a 160-bit (20-byte) hash value.
  - 4. Hex Encoding and Upper Case Conversion: From the SHA1 hash, bytes 2 to 10 are extracted and converted into a hexadecimal string. This string is then transformed into uppercase letters to standardize the format.
  - 5. Output: The resulting uppercase hexadecimal string is the checksum.

### Usage

To use the script, define the token, payload, and signature variables with the appropriate values. Then, run the script to generate the checksum. The output will be the calculated checksum based on the provided inputs.
