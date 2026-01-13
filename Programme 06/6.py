def decrypt_advanced(encrypted, interval):
    return encrypted[::interval]

# Example
encrypted_text = "sxyexynxydxy cxyhxyexyexysxye"
interval = 3
print(decrypt_advanced(encrypted_text, interval))