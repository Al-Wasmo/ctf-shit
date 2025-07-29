import re
import codecs
import codecs
import base64
import hashlib
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish



def lII(file_name: str):
    # Extract substring between 'ä' and 'ü'
    start = file_name.index('ä') + 1
    end = file_name.rindex('ü')
    sliced = file_name[start:end]
    
    # Split by 'ö'
    l = sliced.split('ö')
    return l


def decrypt_des_base64(ciphertext_b64: str, key_str: str) -> str:
    # Step 1: Get MD5 of key string, take first 8 bytes
    md5_key = hashlib.md5(key_str.encode('utf-8')).digest()
    des_key = md5_key[:8]

    # Step 2: Create DES cipher (ECB mode, no IV)
    cipher = DES.new(des_key, DES.MODE_ECB)

    # Step 3: Decode Base64 and decrypt
    encrypted_bytes = base64.b64decode(ciphertext_b64)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Step 4: Remove padding if any (e.g., PKCS5/PKCS7)
    pad_len = decrypted_bytes[-1]
    if all(b == pad_len for b in decrypted_bytes[-pad_len:]):
        decrypted_bytes = decrypted_bytes[:-pad_len]

    return decrypted_bytes.decode('utf-8')


# original search string (escaped form)
search_pattern = r'\\u0082\\u0091\\u00bdUUUUUUUU'

lines = "" 
with open("BadApplePlayer.java", "r", encoding="utf-8") as f:
    for lineno, line in enumerate(f, 1):
        if re.search(search_pattern, line):
            lines = line
            # print(f"[Line {lineno}]: {line.strip()}")

lines = lines.replace('")).getBytes(StandardCharsets.ISO_8859_1);',"")
lines = lines.replace('") + new String("',"")
lines = lines.replace('a = (new String("',"")
lines = lines.replace("        ","")

data = codecs.decode(lines, "unicode_escape")
raw_bytes = data.encode("latin1")

with open("data2-extract","wb") as f:
    f.write(raw_bytes)


# print(raw_bytes)
import re

# This is the raw string from Java
target_java_string = r'(new String("\u00c6\u00d9EUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'

# Escape it for regex matching
search_pattern = re.escape(target_java_string)

prev_linee = ""
prev_line = ""
lines_found = []

with open("BadApplePlayer.java", "r", encoding="utf-8") as f:
    for lineno, line in enumerate(f, 1):
        if re.search(search_pattern, line):
            lines = line



file_name = "äHDoYkHCBuaQ=öuuonuöDhcdDA0xöVsxnxöeWw4tNbrZEo+hzkzKMBLUfuRrBmhubxarnpUWqLVG4dPlhRyv+i7kYSUxO5x9i2qWS9jLWZDh3VFX29jtO185d5ea+9x4fV9Z4E7z8W2Sn17rVPsXnulssAwViw/1YftggL5vrZbShGEJsoUPPJAkjyeK5o/DD9MC1sBrLko5MvLSXBUpfD4BBhl3i0rs5AyCPby67FG99VoUj/P3ACQpXJZmaa7uWzec3MAQy3Pj5Jp+oUhakVRPlacv6FU7m/FPfMlO7KENa+VSoXvdK46wkjPPuxDxU2z0JgtTK2+fFqTAc/QirSOKQb5RCTLVZSfmcMzF1gufkAFwVRVgEjiScnWXP8S2oVc+EmEuCQq04CDExuFUUoeoGUYnn621NqCdMDWX5TpzfhLWbXwC+VqMJBfKNLyCDUon9FBvqLg7OycYc9Khe1o6NqOY7NzGrI7öcLsCuöü"
result = lII(file_name)


more = decrypt_des_base64(result[4], result[5])

lines = lines.replace('")).getBytes(StandardCharsets.ISO_8859_1);',"")
lines = lines.replace('") + new String("',"")
lines = lines.replace('a = (new String("',"")
lines = lines.replace("        ","")
lines = lines.replace('") + new String(I[2])).getBytes(StandardCharsets.ISO_8859_1);',"")
lines += more

data = codecs.decode(lines, "unicode_escape")
raw_bytes = data.encode("latin1")

# print(raw_bytes)

with open("data2-extract","ab") as f:
    f.write(raw_bytes)