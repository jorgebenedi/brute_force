# brute_force
dictionary_attack
This script is designed to crack hashed passwords by comparing them against a wordlist (kaonashi.txt). It supports several hash algorithms including MD5 (32-character hashes), SHA1 (40-character hashes), SHA256 (64-character hashes), and SHA512 (128-character hashes). The user inputs a hash, and the script automatically detects the hash type based on its length. It processes the wordlist in batches for efficiency and compares each word to the hash. If a match is found, the original plaintext word is displayed. Features include batch processing for handling large wordlists efficiently, automatic hash type detection, and support for interrupt handling (Ctrl+C) to exit gracefully.

hash_generator
This script generates cryptographic hashes from user input using common algorithms such as MD5, SHA1, SHA256, and SHA512. The user selects an algorithm from a simple menu and inputs a plaintext string to hash. The script then outputs the resulting hash in hexadecimal format. Features include a simple, menu-driven interface, support for UTF-8 encoding for input, and a clean exit if an interrupt occurs or invalid input is provided.

dictionary_generator
This script creates a customizable wordlist (dictionary) for password attacks or testing purposes. Users can specify the desired length of words and choose whether to include lowercase letters, uppercase letters, digits, and symbols. The generated combinations are written to a text file, which can then be used in dictionary-based attacks or password strength evaluations.

