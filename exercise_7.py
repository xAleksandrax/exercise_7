import random
import string


def create_substitution_cipher():
    """
    Creates a monoalphabetic substitution cipher by shuffling the English alphabet.

    Returns:
        dict: A dictionary representing the substitution cipher.
    """
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}


def apply_substitution_cipher(text, cipher):
    """
    Applies a substitution cipher to the given text.

    Args:
        text (str): The input text to be encrypted.
        cipher (dict): The substitution cipher dictionary.

    Returns:
        str: The encrypted text after substitution.
    """
    return ''.join(cipher.get(c, c) for c in text.lower())


def columnar_transposition(text, key_length):
    """
    Applies columnar transposition to the given text.

    Args:
        text (str): The input text to be transposed.
        key_length (int): The number of columns for transposition.

    Returns:
        str: The text after columnar transposition.
    """
    n = len(text)
    extra_chars = key_length - (n % key_length)
    text += ' ' * extra_chars  
    columns = [''] * key_length
    for i in range(n):
        columns[i % key_length] += text[i]
    return ''.join(columns)


def row_transposition(text, key_length):
    """
    Applies row transposition to the given text.

    Args:
        text (str): The input text to be transposed.
        key_length (int): The number of columns (same as in columnar transposition).

    Returns:
        str: The text after row transposition.
    """
    rows = [text[i:i + key_length] for i in range(0, len(text), key_length)]
    random.shuffle(rows)
    return ''.join(rows)


def encrypt(text):
    """
    Encrypts the given text using a combination of substitution cipher and
    transposition techniques (columnar and row transposition).

    Args:
        text (str): The input text to be encrypted.

    Returns:
        str: The fully encrypted text.
    """
    # Substitution cipher
    substitution_cipher = create_substitution_cipher()
    substituted_text = apply_substitution_cipher(text, substitution_cipher)

    # Columnar transposition
    key_length = 10  
    transposed_columns = columnar_transposition(substituted_text, key_length)

    # Row transposition
    encrypted_text = row_transposition(transposed_columns, key_length)

    return encrypted_text


# Example text
text = (
    "The quick brown fox jumps over the lazy dog. This is a sample text to demonstrate the "
    "encryption process. We will encrypt this text using our custom cipher, which involves "
    "substitution and transposition techniques. The result should be a seemingly random and "
    "unintelligible string of characters. Encryption is a process that transforms readable text "
    "into an unreadable format, which can only be converted back to the original text by someone "
    "who possesses the decryption key. This is commonly used to protect sensitive information from "
    "unauthorized access. In our example, we are combining a substitution cipher with columnar and "
    "row transposition methods. The substitution cipher replaces each letter of the alphabet with "
    "another letter, creating an encoded message that is difficult to decipher without knowing the "
    "specific letter mappings. Following this, we apply a columnar transposition, which rearranges "
    "the text into columns and reads them in a specific order, further obfuscating the original "
    "message. Finally, a row transposition shuffles the rows, adding an additional layer of "
    "complexity to the encryption. By using these combined methods, we aim to create a robust "
    "encryption scheme that is not easily broken. Cryptography has a rich history and has evolved "
    "significantly over the centuries. From ancient methods like the Caesar cipher to modern "
    "algorithms that secure digital communications, the field continues to develop in response to "
    "new challenges. In our digital age, encryption is vital for ensuring the privacy and security "
    "of data, enabling secure communication, and protecting against cyber threats. This example "
    "demonstrates the fundamental principles behind more complex encryption techniques used today. "
    "Understanding these basics provides a foundation for exploring more advanced cryptographic "
    "methods and their applications. We hope this example sheds light on the intriguing world of "
    "cryptography and the ongoing efforts to secure our digital information."
)

encrypted_text = encrypt(text)
