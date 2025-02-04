import re

def baca_file_txt_huruf_angka(nama_file):
    try:
        with open(nama_file, 'r') as file:
            # Membaca isi file
            isi_file = file.read()
            
            # Menggunakan regular expression untuk menyaring huruf a-z, A-Z, dan angka 0-9
            kata_kata = re.findall(r'\b[a-zA-Z0-9]+\b', isi_file)
            
            # Menampilkan hasil
            print(f"Total kata yang terdeteksi: {len(kata_kata)}")
            print("\nBeberapa kata yang hanya mengandung huruf a-z, A-Z, atau angka 0-9:\n", kata_kata[:20])  # Menampilkan hanya 20 kata pertama
            
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
nama_file = 'Etika Profesi.txt'
baca_file_txt_huruf_angka(nama_file)
