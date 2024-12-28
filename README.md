# Dictionary-Attack
## Description

This tool is a Python script designed to perform a dictionary attack against a POP3 mail server. It systematically attempts to log in using a list of passwords from a wordlist file. The script supports both unencrypted connections (port 110) and SSL-encrypted connections (port 995), making it versatile for different server configurations.

> **Warning:** This tool is intended for educational purposes or testing systems that you own or have explicit permission to test. Unauthorized use of this tool is illegal and unethical.

---

## Features

- Supports both unencrypted POP3 (port 110) and SSL-encrypted POP3 (port 995).
- Reads passwords from a user-provided wordlist file.
- Provides detailed feedback for each login attempt, indicating success or failure.

---

## Requirements

- Python 3.6 or higher

---

## Usage

### Running the Script

1. Clone or download this repository.
2. Create or obtain a wordlist file containing potential passwords, with each password on a new line (e.g., `wordlist.txt`).
3. Run the script using the following command:
   ```bash
   python pop3_attack.py <server> <port> <username> <wordlist_file> <use_ssl>
   ```

### Parameters

- `<server>`: The POP3 server address (e.g., `pop.mailserver.com`).
- `<port>`: The POP3 port (110 for unencrypted, 995 for SSL).
- `<username>`: The email username for which passwords will be tested.
- `<wordlist_file>`: The path to the password wordlist file.
- `<use_ssl>`: Specify `True` for SSL connections or `False` for unencrypted connections.

### Example

```bash
python pop3_attack.py pop.gmail.com 995 user@example.com wordlist.txt True
```

---

## Example Output

```
Trying password: password123
[FAILED] Incorrect password: password123
Trying password: qwerty
[FAILED] Incorrect password: qwerty
Trying password: mysecurepassword
[SUCCESS] Password found: mysecurepassword
```

---

## Error Handling

- If the wordlist file is not found, the script will display an error message and exit.
- If the server is unreachable or an unexpected error occurs, the script will log the error and either continue or exit, depending on the situation.

---

## Ethical Use

This tool is designed solely for:

1. Testing the security of your own systems.
2. Educational purposes to understand the mechanics of dictionary attacks.

**Do not use this tool without explicit authorization. Unauthorized access to systems is illegal and punishable by law.**

---

## License

This project is licensed under the MIT License. For more information, see the LICENSE file included in the repository.

---

## Contributions

Contributions, bug reports, and feature requests are welcome. To contribute, please submit a pull request or open an issue in this repository.
