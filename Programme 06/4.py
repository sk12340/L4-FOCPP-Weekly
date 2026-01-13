def encrypt_basic(text):
    no_spaces = text.replace(" ", "")
    return no_spaces[::-1]

print(encrypt_basic("send cheese"))