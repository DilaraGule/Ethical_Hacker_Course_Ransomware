import os
from cryptography.fernet import Fernet  # symmetric encryption

file_list = []
for file in os.listdir():
    if file == "ransom.py" or \
            file == "generatedkey.key" or \
            file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):    # dosya kontrolü
        file_list.append(file)

with open("generatedkey.key", "rb") as generatedkey:   # wb: Write binary
    secret_key = generatedkey.read()

for file in file_list:
    with open(file, "rb") as the_file:  # rb: read binary
        contents = the_file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_decrypted)
