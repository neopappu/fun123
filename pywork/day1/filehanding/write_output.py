#!/usr/bin/env python3
import random
import string
import random
import string
import random
import string
import os

output_file = "output.txt"
random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

if os.path.exists(output_file):
    print(f"{output_file} exists.")
else:
    print(f"{output_file} does not exist.")

with open(output_file, "a") as file_handle:
    file_handle.write(random_text + "\n")
print(f"Written: {random_text}")
