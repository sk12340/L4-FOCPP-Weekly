import random
import string

def encrypt_advanced(msg):
    interval = random.randint(2, 20)
    msg_no_spaces = msg.replace(" ", "")
    result = []
    for i, ch in enumerate(msg_no_spaces):
        result.append(ch)
        if i != len(msg_no_spaces) - 1:
            # Adding random letters
            random_letters = ''.join(random.choices(string.ascii_lowercase, k=interval-1))
            result.append(random_letters)
    return ''.join(result), interval

encrypted, interval = encrypt_advanced("send cheese")
print(f"Encrypted: {encrypted}")
print(f"Interval: {interval}")