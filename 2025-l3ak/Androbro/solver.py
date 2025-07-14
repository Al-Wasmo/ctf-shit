from base64 import b64decode
from Crypto.Cipher import AES

# Provided base64-encoded strings
BASE64_KEY = "QZrwuDw4+lFrKFRvznVl3A=="
BASE64_IV = "Z4drGE7JIeRhwjFxxw4kcA=="
BASE64_ENCRYPTED_FLAG = "LbkzN+Zr+k6klBtEh0jWnGX6zjTPXXTCztliM8++ENqdkWdyT5nkPn3yQ2YCXh9oBpvd9ab7AKS2JJ2i5YBj+Q=="

# Decode all inputs
key = b64decode(BASE64_KEY)
iv = b64decode(BASE64_IV)
ciphertext = b64decode(BASE64_ENCRYPTED_FLAG)

# Decrypt using AES-CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Unpad (PKCS#5/PKCS#7)
pad_len = plaintext[-1]
flag = plaintext[:-pad_len].decode('utf-8')

print("[+] Decrypted Flag:", flag)
