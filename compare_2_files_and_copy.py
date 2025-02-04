def normalize_key(key):
    return key.strip().upper()

def compare_and_merge_files(file_a, file_b, file_c):
    entries = {}

    # Fungsi bantu untuk membersihkan dan normalisasi baris
    def clean_line(line):
        if '=' in line:
            key, value = line.strip().split('=', 1)
            return normalize_key(key), value.strip()
        return None, None

    # Baca file B terlebih dahulu (agar tetap dominan)
    with open(file_b, 'r', encoding='utf-8') as fb:
        for line in fb:
            key, value = clean_line(line)
            if key:
                entries[key] = value

    # Baca file A dan tambahkan yang belum ada di B
    with open(file_a, 'r', encoding='utf-8') as fa:
        for line in fa:
            key, value = clean_line(line)
            if key and key not in entries:
                entries[key] = value

    # Tulis hasil gabungan ke file C tanpa duplikasi
    with open(file_c, 'w', encoding='utf-8') as fc:
        for key, value in sorted(entries.items()):
            fc.write(f"{key} = {value}\n")

    print(f"Proses selesai! File hasil telah disimpan sebagai '{file_c}' dengan ukuran {fc.tell() / 1024 / 1024:.2f} MB")

# Contoh penggunaan
compare_and_merge_files('global_A.oxt', 'global_B.oxt', 'global_C.oxt')