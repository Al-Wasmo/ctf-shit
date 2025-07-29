import codecs
import base64
import hashlib
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish

def decrypt(base64_input: str, key: str) -> str:
    decoded = base64.b64decode(base64_input).decode('utf-8')
    key_chars = list(key)
    result = []

    for i, c in enumerate(decoded):
        result.append(chr(ord(c) ^ ord(key_chars[i % len(key_chars)])))

    return ''.join(result)


# print(decrypt("FwwzSQoYESMIDxpCNkkFGQwjSRceAyNJEAMSJwYRAhF3KxEXCzsFBlYBPwgRFwEjDBEFTHdXQ+KhpEJr", "vbWic"))
# print(decrypt("JCIwBQZUFTsCEAZwIRlVByQ0BAFafns=", "tPUvu"))
# print(decrypt("RQ==", "ebOAi").encode())
# print(decrypt("STdVD3Z3CDg=", "RlpkM").encode(),"reset")
# print(decrypt("cQ1lc28C", "jVZAZ").encode())




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



# print(decrypt_des_base64("CG74vN7titk=", "Xnezh").encode())
# print(decrypt_des_base64("nwlWvVqWpkg=", "OWngd").encode())
# print(decrypt_des_base64("5+wZKWqT600=", "llptX").encode())
# print(decrypt_des_base64("+W3ZSoQaQzb8tsZvhtYf7FsECf16KPOtaLkHkpY2nF+nS2bhVzDH/iQDQzuskkJfZX46oI2ZmSKd+4KOvmdGbjGz69hNUS92R+me+KTVIb5+jaSKSxM2jub6EIu6je+stEsph9QMW0uyDfML4rsK/vyHS3l0ZSgt+8B+6bf+Qtmz6TEXI75mlcEza2r3eM6zF5N7BfSlTx65JwC4ECeBTOS/n5Tt/xLlWFf/e9gQi1e+hFwDEsUqnGTfb8WLSw1ddn95c9XJV5jqe9V7sb7XpO74SkZ4qUpTC03xzPT/R6YYbSKqhw1q1IxlgCuHu9TC32exFUc9ezjHj1h6Db8ARreH/vUE64vim/O1HXcxjZ9W/gJi1PHkVLyK84KlyOr3KaJN6fvrSlstilLg7lvzMLmgd2irpo6xkeGDuIobZdqLaPrUtGqLgZRz3FM7dhUUnFllq0LwGPcyDtGdV+dSPg7LMMRuax5BgqMCwP3/wGEliy0TiQBJNEyfu4DsPe88oFCrwzFUn5GMYaddqL6BHhFHnTM3Yoiadh6rWzRajiI1GO+uTveptyvGgoPjrohrx6hIYN02rRV90odpN1VyxrPrlmGmipQ6Lgh5BQphbxwBytZafe9jnWaXh0GGpJ0+9KfOH6GuFWDBcP+il/QirK8DSlq66XcIhyjtOCAebyiW3hk7UkrIpmdAUZvnQtNwQZG7GGmVGXZZhKlTkEAtAF7QBLylBzdwpyB7N14JnkSY6/PIvu4ljjWcQQOAnVKO74Vb7RgKAV8Vwi25f/NlconyuPpVMJcDwm0TTQ/vB0xKwe4z0qm9JiBGrFbf4SqWj7A1WfKifhNL2N0+fnMjokNft3fBBjYaPc4fv+IEWOCklB2b1NJ9Bex/dKcm+wZ7XKkqRv5KBg9qVNOFgSAWFPG61z9D/sBRHzn3F8gLbPSJ2hROALEZDtyLcZzbiV0oIOgPz6dp0HKKHoELMYhgFU9WtC1dpUije8gjYXYIg7ZMn1ZO9uybgnG64XcQ6YJGxnnZCMt6Sx0=", "Qmfbd").encode())



def decrypt_blowfish_base64(ciphertext_b64: str, key_str: str) -> str:
    # Step 1: Generate MD5 hash of key
    key_md5 = hashlib.md5(key_str.encode('utf-8')).digest()

    # Step 2: Initialize Blowfish cipher (ECB mode)
    cipher = Blowfish.new(key_md5, Blowfish.MODE_ECB)

    # Step 3: Base64 decode and decrypt
    encrypted_data = base64.b64decode(ciphertext_b64)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Step 4: Remove padding (PKCS-style, if used)
    pad_len = decrypted_data[-1]
    if all(b == pad_len for b in decrypted_data[-pad_len:]):
        decrypted_data = decrypted_data[:-pad_len]

    return decrypted_data.decode('utf-8')


# print(decrypt_blowfish_base64("5DgmZ40SxnXDwhqEU2Mn7N0FAvLGb4Ct5IovLPFbKAM0tTQsGPFswX0gWJYud6rOWsiQF4//0U9x+bI6M7TDSPnKG+YhD17B", "zIDpX").encode())
# print(decrypt_blowfish_base64("GWqqf9K7DBQ=", "mbueV").encode())
# print(decrypt_blowfish_base64("KQdwo72Q1yc=", "NgsYz").encode())
# print(decrypt_blowfish_base64("SNCL8E6RunAHedoXguLIKg==", "hyKyw").encode())
# print(decrypt_blowfish_base64("eFjKzLVXQrDhlH7LFnJecw==", "mWHlZ").encode())
# print(decrypt_des_base64("UTDQDfEVmw4=", "YQcfb").encode())
# print(decrypt_des_base64("5+wZKWqT600=", "llptX").encode())
# print(decrypt_des_base64("+W3ZSoQaQzb8tsZvhtYf7FsECf16KPOtaLkHkpY2nF+nS2bhVzDH/iQDQzuskkJfZX46oI2ZmSKd+4KOvmdGbjGz69hNUS92R+me+KTVIb5+jaSKSxM2jub6EIu6je+stEsph9QMW0uyDfML4rsK/vyHS3l0ZSgt+8B+6bf+Qtmz6TEXI75mlcEza2r3eM6zF5N7BfSlTx65JwC4ECeBTOS/n5Tt/xLlWFf/e9gQi1e+hFwDEsUqnGTfb8WLSw1ddn95c9XJV5jqe9V7sb7XpO74SkZ4qUpTC03xzPT/R6YYbSKqhw1q1IxlgCuHu9TC32exFUc9ezjHj1h6Db8ARreH/vUE64vim/O1HXcxjZ9W/gJi1PHkVLyK84KlyOr3KaJN6fvrSlstilLg7lvzMLmgd2irpo6xkeGDuIobZdqLaPrUtGqLgZRz3FM7dhUUnFllq0LwGPcyDtGdV+dSPg7LMMRuax5BgqMCwP3/wGEliy0TiQBJNEyfu4DsPe88oFCrwzFUn5GMYaddqL6BHhFHnTM3Yoiadh6rWzRajiI1GO+uTveptyvGgoPjrohrx6hIYN02rRV90odpN1VyxrPrlmGmipQ6Lgh5BQphbxwBytZafe9jnWaXh0GGpJ0+9KfOH6GuFWDBcP+il/QirK8DSlq66XcIhyjtOCAebyiW3hk7UkrIpmdAUZvnQtNwQZG7GGmVGXZZhKlTkEAtAF7QBLylBzdwpyB7N14JnkSY6/PIvu4ljjWcQQOAnVKO74Vb7RgKAV8Vwi25f/NlconyuPpVMJcDwm0TTQ/vB0xKwe4z0qm9JiBGrFbf4SqWj7A1WfKifhNL2N0+fnMjokNft3fBBjYaPc4fv+IEWOCklB2b1NJ9Bex/dKcm+wZ7XKkqRv5KBg9qVNOFgSAWFPG61z9D/sBRHzn3F8gLbPSJ2hROALEZDtyLcZzbiV0oIOgPz6dp0HKKHoELMYhgFU9WtC1dpUije8gjYXYIg7ZMn1ZO9uybgnG64XcQ6YJGxnnZCMt6Sx0=", "Qmfbd").encode())


# print(decrypt("STdVD3Z3CDg=", "RlpkM").encode(),"reset")
# print(decrypt_blowfish_base64("KQdwo72Q1yc=", "NgsYz").encode())
# print(decrypt_blowfish_base64("SNCL8E6RunAHedoXguLIKg==", "hyKyw").encode())


# a = decrypt_des_base64("9Ukf4cvsFzNNl+B3/olHum0HJQ5Zl4bODQ9wvdiXEzwOpml4HcFaefJdWnLUoNiqu5Kq3XRKYnP1SR/hy+wXM02X4Hf+iUe6bQclDlmXhs4ND3C92JcTPA6maXgdwVp58l1actSg2KqHuEk2zm1/ZciXKeoSLM6oRrmwEizA2VUooxlXnAW/Ilahz65l5C60b/nL/qehjBmBx9rs/UmN/TMBRALYRrKHHw6RvKjpHVrQfw9PSudsPiijGVecBb8iVqHPrmXkLrRv+cv+p6GMGYHH2uz9SY39MwFEAthGsocfDpG8qOkdWtB/D09K52w+KKMZV5wFvyJWoc+uZeQutG/5y/6noYwZgcfa7P1Jjf0zAUQC2Eayhx8Okbyo6R1a0H8PT0rnbD4ooxlXnAW/IvutRugqfw/D", "Yyyir").encode()

# data = ""
# with open("main.py","r") as f:
#     data = f.read().split("\n")[0]


# data = data.replace('''") + new String("''',"").replace('new String("',"")


# data = codecs.decode(data, "unicode_escape")
# raw_bytes = data.encode("latin1")

# with open("file","wb") as f:
#     f.write(raw_bytes + a)


def lII(file_name: str):
    # Extract substring between 'ä' and 'ü'
    start = file_name.index('ä') + 1
    end = file_name.rindex('ü')
    sliced = file_name[start:end]
    
    # Split by 'ö'
    l = sliced.split('ö')
    return l


file_name = "äHDoYkHCBuaQ=öuuonuöDhcdDA0xöVsxnxöeWw4tNbrZEo+hzkzKMBLUfuRrBmhubxarnpUWqLVG4dPlhRyv+i7kYSUxO5x9i2qWS9jLWZDh3VFX29jtO185d5ea+9x4fV9Z4E7z8W2Sn17rVPsXnulssAwViw/1YftggL5vrZbShGEJsoUPPJAkjyeK5o/DD9MC1sBrLko5MvLSXBUpfD4BBhl3i0rs5AyCPby67FG99VoUj/P3ACQpXJZmaa7uWzec3MAQy3Pj5Jp+oUhakVRPlacv6FU7m/FPfMlO7KENa+VSoXvdK46wkjPPuxDxU2z0JgtTK2+fFqTAc/QirSOKQb5RCTLVZSfmcMzF1gufkAFwVRVgEjiScnWXP8S2oVc+EmEuCQq04CDExuFUUoeoGUYnn621NqCdMDWX5TpzfhLWbXwC+VqMJBfKNLyCDUon9FBvqLg7OycYc9Khe1o6NqOY7NzGrI7öcLsCuöü"
result = lII(file_name)
print(decrypt_des_base64(result[4], result[5]).encode())
