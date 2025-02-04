import random
import string

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_text_file(filename, count):
    seen_strings = set()
    with open(filename, 'w') as f:
        while len(seen_strings) < count:
            random_string = generate_random_string(10)
            if random_string not in seen_strings:
                seen_strings.add(random_string)
                f.write(f"\"{random_string}\":\n")

# Menentukan jumlah baris yang diinginkan
num_lines = 1000
# Menyimpan hasil ke dalam file "output.txt"
generate_text_file("output.txt", num_lines)
print(f"{num_lines} baris teks telah ditulis ke dalam file 'output.txt'.")
