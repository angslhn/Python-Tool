import os

def get_all_files(folder_path):
    """
    Mendapatkan semua file di dalam folder beserta subfoldernya.
    """
    all_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Menyimpan path relatif file
            relative_path = os.path.relpath(os.path.join(root, file), folder_path)
            all_files.append(relative_path)
    return all_files

def find_missing_files(folder_a, folder_b):
    """
    Menemukan file yang ada di folder_a tetapi tidak ada di folder_b.
    """
    files_a = set(get_all_files(folder_a))
    files_b = set(get_all_files(folder_b))

    # Mencari file yang ada di folder_a tapi tidak ada di folder_b
    missing_files = files_a - files_b

    return missing_files

def main():
    folder_a = r'C:\Users\Aang Solihin\Pictures\Folder A'  # Ganti dengan path folder_a yang sesuai
    folder_b = r'C:\Users\Aang Solihin\Pictures\Folder B'  # Ganti dengan path folder_b yang sesuai

    missing_files = find_missing_files(folder_a, folder_b)

    if missing_files:
        print("File yang hilang di folder_b:")
        for file in missing_files:
            print(f"{file} tidak ditemukan di folder_b")
    else:
        print("Tidak ada file yang hilang di folder_b.")

if __name__ == "__main__":
    main()