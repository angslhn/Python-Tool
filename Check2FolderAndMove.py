import os
import shutil

# Buat path untuk folder A, B dan C
folder_a = r"C:\Users\Aang Solihin\Pictures\VEHICLES PROP A"
folder_b = r"C:\Users\Aang Solihin\Pictures\VEHICLES PROP B"
folder_c = r"C:\Users\Aang Solihin\Pictures\VEHICLES PROP C"

# Buat folder C jika belum ada
if not os.path.exists(folder_c):
    os.makedirs(folder_c)

# Dapatkan daftar file di folder A dan folder B
files_in_a = set(os.listdir(folder_a))
files_in_b = set(os.listdir(folder_b))

# Bandingkan folder A dan B, cek file mana yang ada di A tetapi belum ada di B
files_to_move = files_in_a - files_in_b

# Pindahkan file dari folder A yang belum ada di folder B ke folder C
for file_name in files_to_move:
    src_file = os.path.join(folder_a, file_name)
    dst_file = os.path.join(folder_c, file_name)
    shutil.move(src_file, dst_file)
    print(f"Memindahkan file {file_name} dari folder A ke folder C.")

print("Proses selesai.")
