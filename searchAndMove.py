import os
import shutil

def cari_dan_pindahkan_folder(path_target_pencarian, path_target_pemindahan):
    # Mencari semua folder di dalam path_target_pencarian
    for root, dirs, files in os.walk(path_target_pencarian):
        # Cek setiap folder dalam root
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            # Mencari file dengan ekstensi .msg.22 dalam folder tersebut
            if any(file.endswith(".msg.22") for file in os.listdir(folder_path)):
                print(f"Ditemukan folder dengan file .msg.22: {folder_path}")
                # Memindahkan folder ke path_target_pemindahan
                target_folder_path = os.path.join(path_target_pemindahan, os.path.basename(folder_path))
                shutil.move(folder_path, target_folder_path)
                print(f"Folder {folder_path} dipindahkan ke {target_folder_path}")

# Contoh penggunaan:
if __name__ == "__main__":
    path_target_pencarian = r"C:\Users\Aang Solihin\Pictures\Unpack"
    path_target_pemindahan = r"C:\RE Message Tool"

    cari_dan_pindahkan_folder(path_target_pencarian, path_target_pemindahan)
