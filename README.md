# 🔐 INSA Summer Talent 2026 – Cryptography Practical Assessment

This repository contains my solutions for the **INSA Summer Talent 2026 Cryptography Practical Assessment**. The project demonstrates fundamental concepts of cryptography, including file hashing, classical encryption algorithms, password authentication, and file integrity verification using Python and Windows command-line tools.

---

## 📌 Project Objectives

This project covers the following cryptography concepts:

- File operations and cryptographic hashing
- File integrity verification
- Classical encryption algorithms
- Password authentication using SHA-256
- Understanding the Avalanche Effect
- Basic cybersecurity principles

---

## 📂 Repository Structure

```
.
├── Caesar.py          # Caesar Cipher implementation
├── Vigenère.py        # Vigenère Cipher implementation
├── password.py        # SHA-256 password authentication
├── message.txt        # Sample text file
├── md5.txt            # MD5 hash output
├── sha1.txt           # SHA-1 hash output
├── sha256.txt         # SHA-256 hash output
└── README.md          # Project documentation
```

---

## ✅ Task 1 – File Operations & Hashing

This task demonstrates how cryptographic hash functions can verify file integrity.

### Completed

- Created `message.txt`
- Displayed file contents
- Generated MD5, SHA-1, and SHA-256 hashes
- Saved each hash into separate files
- Modified one character in the original file
- Generated a new SHA-256 hash
- Compared both hashes
- Demonstrated the **Avalanche Effect**

---

## ✅ Task 2 – Classical Cryptography

Implemented two classical encryption algorithms:

### Caesar Cipher

- User-defined shift value
- Encrypt plaintext
- Decrypt ciphertext

### Vigenère Cipher

- User-defined keyword
- Encrypt plaintext
- Decrypt ciphertext

---

## ✅ Task 3 – Hashing & Password Authentication

Implemented a simple authentication system using SHA-256.

### Features

- Store the SHA-256 hash of a password
- Accept password input from the user
- Hash the entered password
- Compare hashes
- Display authentication status

Output:

```
Authentication Successful
```

or

```
Authentication Failed
```

---

## 🛠 Technologies Used

- Python 3
- Windows Command Prompt
- Cryptographic Hash Functions
- SHA-256
- SHA-1
- MD5

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/ezamuh4-bit/INSA-Summer-Camp-2018-Cryptography-Practical-Assessment-.git
```

### Open the project

```bash
cd INSA-Summer-Camp-2018-Cryptography-Practical-Assessment-
```

### Run the programs

Caesar Cipher

```bash
python Caesar.py
```

Vigenère Cipher

```bash
python Vigenère.py
```

Password Authentication

```bash
python password.py
```

---

## 📖 Key Concepts Learned

- Cryptographic Hash Functions
- File Integrity Verification
- SHA-256
- SHA-1
- MD5
- Password Authentication
- Classical Cryptography
- Caesar Cipher
- Vigenère Cipher
- Avalanche Effect
- Basic Cybersecurity

---

## 📷 Expected Outputs

- Hash values generated using MD5, SHA-1, and SHA-256
- Successful and failed password authentication
- Encryption and decryption of plaintext
- File integrity verification after modifying a file

---

## 👨‍💻 Author

**Ezadin Mohammad Umar**

GitHub: https://github.com/ezamuh4-bit

---

## 📜 License

This repository was created for educational purposes as part of the **INSA Summer Talent 2026 Cryptography Practical Assessment**.
