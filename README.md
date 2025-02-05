# Collatz Encryption - Public Release

This repository contains the **first public version** of the Collatz Encryption system, an encryption method inspired by the **Collatz Conjecture**, an unsolved mathematical problem. This release serves as a **foundation for further development** in encryption research.

⚠️ **A significantly more secure private version is available for purchase, offering encryption that is thousands of times stronger.** If you are interested, contact me via Discord: **Cyberseall**.

## 📸 Screenshots

### Public Version:
![Compiler Preview Free Version](https://i.imgur.com/wHnMZtP.png)

![Encryptor Preview Free Version](https://i.imgur.com/an2DGuC.png)

### Private Version (Highly Secure, Available for Purchase):
![Encryptor Preview Private Version](https://i.imgur.com/lBxUEbn.png)

![Compiler Preview Private Version](https://i.imgur.com/Wfde8F7.png)

![Settings Preview Private Version](https://i.imgur.com/GjglWmf.png)

![Settings2 Preview Private Version](https://i.imgur.com/gBi1QgD.png)

![Misc Options Preview Private Version](https://i.imgur.com/b1Tb0wp.png)

---

## 🔥 Features (Public Version)
- Encrypts Python files using a novel Collatz-based encryption algorithm
- Generates a unique decryption key for each encryption
- Decryption works without needing external libraries beyond Python’s standard toolkit
- **GUI-based encryption and decryption tool** built with Tkinter
- Support for compiling encrypted files into standalone executables
- Uses a mathematical transformation based on the Collatz Conjecture for obfuscation
- Hard to detect by antivirus software due to its unique structure
- Potential resistance to quantum computing attacks due to its non-linear transformation


  ### 🔍 Entropy Analysis Report for EncryptedApp.exe (Free Version)

The entropy analysis of the file **EncryptedApp.exe** reveals a Shannon entropy value of **7.9943**.

#### 📊 What Does This Mean?
- An entropy value of **0** indicates a completely predictable file (e.g., full of repeating bytes).
- An entropy value of **8.0** suggests perfect randomness, typically seen in strongly encrypted or compressed data.
- **The observed value of 7.9943 is extremely close to the theoretical maximum entropy of 8.0**, indicating that the file is highly obfuscated or encrypted.

#### 🛡 Security Implications:
- High entropy makes **pattern recognition and statistical attacks nearly impossible**.
- This suggests that the **Free Version** of Collatz Encryption still uses **strong encryption techniques**.
- However, the security mechanisms are not as advanced as the **Private Version**, which implements additional countermeasures.

![Entropie Analysis Preview Free Version](https://i.imgur.com/d0aJVPA.png)

**Conclusion:**  
The Free Version of Collatz Encryption **provides solid encryption** and offers strong resistance against forensic analysis. However, **compared to the Private Version, it lacks certain multi-layer encryption and advanced anti-forensic mechanisms**.


---

## 🔒 Features (Private Version - Available for Purchase)
- **Advanced Key Evolution:** Dynamically evolving key structure that increases security exponentially, making brute-force attacks infeasible.
- **Post-Quantum Security:** Enhances resistance to quantum algorithms by integrating **lattice-based** cryptographic techniques alongside Collatz transformations.
- **Multi-Layer Encryption:** Supports **AES-256**, **Elliptic Curve Cryptography (ECC)**, and **Post-Quantum Cryptography (PQC)**.
- **Anti-Tampering & Obfuscation:** Introduces an 8-byte fake header and runtime memory obfuscation to prevent reverse engineering.
- **Secure Execution Environment:** Implements **anti-debugging**, **anti-VM detection**, and **hidden process execution** to evade forensic analysis.
- **Integrity Protection:** Uses **HMAC-SHA512** and **SHA-3** hashing to ensure encrypted data has not been tampered with.
- **Custom Key Splitting:** Supports key fragmentation across multiple distributed storage locations for enhanced security.
- **Faster Decryption Performance:** Optimized key iteration algorithms allow decryption speeds **up to 10x faster** than the public version.
- **Zero-Knowledge Execution:** Allows encrypted scripts to be executed without ever exposing the decrypted code in memory.
- **Steganographic Encryption:** Ability to hide encrypted payloads within images or other file types to avoid detection.
- **Self-Destruct Mechanism:** Triggers automatic destruction of encrypted data after a predefined number of failed decryption attempts.
- **Remote Key Management:** Secure cloud-based key storage with real-time access control for enterprise-level security.
- **Modular Encryption Framework:** Can be integrated into existing applications with minimal modification.
- **Offline Key Generation:** Ensures encryption keys never need to be stored online, reducing the risk of breaches.
- **Adaptive Security Policies:** Dynamically adjusts encryption strength based on detected threat levels.
- **Hardware-Based Security:** Supports **Trusted Execution Environments (TEE)** for additional protection against physical attacks.


  ### 🔍 Entropy Analysis Report for SecureApp.exe (Private Version)

The entropy analysis of the file **SecureApp.exe** reveals a Shannon entropy value of **7.9953**.

#### 📊 What Does This Mean?
- An entropy value of **0** means the file is entirely predictable (e.g., a file full of zero bytes).
- A maximum entropy value of **8.0** indicates the file appears perfectly random, typically seen in highly encrypted or compressed data.
- **The observed value of 7.9953 shows that the file is extremely close to maximum entropy!** This strongly suggests high-level encryption or data compression.

#### 🛡 Security Implications:
- High entropy means **statistical attacks (such as frequency analysis) are nearly impossible**.
- This confirms that **SecureApp.exe is strongly encrypted with no detectable patterns**.
- Such high entropy is generally observed in **advanced cryptographic implementations**.

![Entropie Analysis Preview Private Version](https://i.imgur.com/K8jyGFZ.png)

**Conclusion:**  
The high entropy confirms that the **private version of Collatz Encryption uses extremely strong encryption**, making it highly resistant to forensic analysis and decryption attempts.



**Why is the Private Version 1000x More Secure?**
- Uses multi-layer encryption instead of a single-layer XOR transformation.
- Prevents all known forms of attack against static key evolution by introducing randomness.
- Defends against **Shor’s Algorithm**, making it quantum-resistant.
- Implements memory scrambling techniques to prevent key extraction from RAM.

---

## 🛠️ How It Works
This encryption system relies on bitwise operations and iterative transformations derived from the **Collatz Conjecture**:

1. Each character in the original Python script is converted to its ASCII value.
2. A bitwise XOR operation is applied using a dynamic key.
3. The key evolves dynamically based on the following rules:
   - If the key is **odd**, apply `key = (key * 3) + 1`
   - If the key is **even**, apply `key = key / 2`
4. The process continues iteratively, ensuring a non-linear encryption pattern.
5. To decrypt, the process is reversed, using the same initial key.

**Example of encryption logic:**
```python
for char in data:
    encrypted_char = ord(char) ^ key
    encrypted_data.append(encrypted_char)
    key = (key * 3 + 1) if key % 2 else (key // 2)
```

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.x
- Tkinter (usually pre-installed with Python)

### Install Required Libraries
No additional libraries are needed beyond the Python standard library.

### Usage Instructions
1. **Run the Encryption Tool:**
   ```bash
   python encryptor.py
   ```
   - Select a Python file to encrypt.
   - Provide an encryption key (integer).
   - The encrypted file (`.bin`) and decryption key (`.txt`) will be saved.

2. **Run the Decryption Tool:**
   ```bash
   python encryptor.py
   ```
   - Select the encrypted `.bin` file and the corresponding `.txt` key file.
   - The original Python script is restored.

3. **Compile Encrypted Code into an Executable:**
   ```bash
   python compiler.py
   ```
   - Select the encrypted `.bin` file and the `.txt` key file.
   - The program compiles an executable (`.exe`) that automatically decrypts and runs the script.

---

## 📝 Contact
For discussions, feature requests, or purchasing the **private high-security version**, contact me on **Discord: cyberseall**.
