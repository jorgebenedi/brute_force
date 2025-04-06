# brute_force

brute_force 
This script is designed to crack hashed passwords by comparing them against a wordlist (kaonashi.txt). It supports the following hash algorithms:

MD5 (32-character hashes)

SHA1 (40-character hashes)

SHA256 (64-character hashes)

SHA512 (128-character hashes)

How it works:

The user inputs a hash.

The script automatically detects the hash type based on its length.

It processes the wordlist in batches (for efficiency) and checks each word against the hash.

If a match is found, the original plaintext word is displayed.

Features:

Batch processing to handle large wordlists efficiently.

Automatic hash type detection.

Supports interrupt handling (Ctrl+C to exit gracefully).

hash_generator
This script generates cryptographic hashes from user input using common algorithms:

MD5

SHA1

SHA256

SHA512

How it works:

The user selects an algorithm from the menu.

Inputs a plaintext string to hash.

The script outputs the hexadecimal hash.

Features:

Simple menu-driven interface.

Supports UTF-8 encoding for input.

Clean exit on interrupt or invalid input.
