import os
import base64
from hashlib import sha256
from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet

def derive_key(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    key = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.urlsafe_b64encode(key), salt

def encrypt_files(input_folder, output_folder, hide_extension, password):
    os.makedirs(output_folder, exist_ok=True)
    salt = os.urandom(16)
    key, _ = derive_key(password, salt)
    fernet = Fernet(key)
    count = 0

    print(" ---------------------------------")
    print("\n -------------------------------------------")

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
            if hide_extension:
                encrypted_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0])
            else:
                encrypted_file_path = os.path.join(output_folder, file_name)

            with open(encrypted_file_path, 'wb') as file:
                file.write(salt + encrypted_data)
            count += 1
            print(f" - FILE '{file_name}' TELAH DI ENKRIPSI")

    print(" -------------------------------------------")
    print("\n ---------------------------------")
    print(f" - {count} FILE BERHASIL DI ENKRIPSI")
    print(" ---------------------------------")

def decrypt_files(input_folder, output_folder, password, add_extension=False, file_extension=None):
    os.makedirs(output_folder, exist_ok=True)
    count = 0

    print(" ------------------------------------")
    print("\n -------------------------------------------")

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()

            salt = file_data[:16]
            encrypted_data = file_data[16:]
            key, _ = derive_key(password, salt)

            fernet = Fernet(key)
            try:
                decrypted_data = fernet.decrypt(encrypted_data)
                if add_extension and file_extension:
                    decrypted_file_path = os.path.join(output_folder, f"{file_name}.{file_extension}")
                else:
                    decrypted_file_path = os.path.join(output_folder, file_name)

                with open(decrypted_file_path, 'wb') as file:
                    file.write(decrypted_data)
                count += 1
                print(f" - FILE '{file_name}' TELAH DI DESKRIPSI")
            except Exception:
                print(f" - FILE '{file_name}' GAGAL DI DESKRIPSI")

    print(" -------------------------------------------")
    print("\n ----------------------------------")
    print(f" - {count} FILE BERHASIL DI DESKRIPSI")
    print(" ----------------------------------")

def main_menu():
    print(" ---------------------------")
    print(" ---------- FUIN -----------")
    print(" ---------------------------")
    print(" - 1. ENKRIPSI")
    print(" - 2. DESKRIPSI")
    print(" ---------------------------")
    choice = input(" - PILIHAN = ").strip()
    print(" ---------------------------")

    if choice == '1':
        print("\n ---------------------------------")
        print(" PROSES INI AKAN MEN-ENKRIPSI FILE")
        print(" ---------------------------------")
        input_folder = input(" - FOLDER FILE = ").strip()
        output_folder = input(" - FOLDER HASIL ENKRIPSI = ").strip()
        
        hide_extension_option = False
        for file_name in os.listdir(input_folder):
            if os.path.isfile(os.path.join(input_folder, file_name)) and '.' in file_name:
                hide_extension_option = True
                break

        hide_extension = 'T'
        if hide_extension_option:
            hide_extension = input(" - SEMBUNYIKAN EKSTENSI FILE (Y/T) = ").strip().upper()
        
        if hide_extension not in ('Y', 'T'):
            print(" - Input tidak valid. Coba lagi.")
            return

        password = input(" - PASSWORD = ").strip()

        if len(password) < 8:
            print(" ----------------------------------")
            print("\n ------------------------------------")
            print(" - Password terlalu pendek. Coba lagi.")
            print(" ------------------------------------")
            return

        encrypt_files(input_folder, output_folder, hide_extension == 'Y', password)

    elif choice == '2':
        print("\n ------------------------------------")
        print(" - PROSES INI AKAN MEN-DESKRIPSI FILE")
        print(" ------------------------------------")
        input_folder = input(" - FOLDER FILE ENKRIPSI = ").strip()
        output_folder = input(" - FOLDER HASIL DESKRIPSI = ").strip()

        hide_extension_option = True
        for file_name in os.listdir(input_folder):
            if os.path.isfile(os.path.join(input_folder, file_name)) and '.' in file_name:
                hide_extension_option = False
                break

        add_extension = False
        file_extension = None

        if hide_extension_option:
            add_extension_input = input(" - TAMBAHAN EKSTENSI FILE (Y/T) = ").strip().upper()
            if add_extension_input == 'Y':
                add_extension = True
                file_extension = input(" - TIPE EKSTENSI FILE = ").strip()
                if not file_extension:
                    print(" - Jenis ekstensi file tidak boleh kosong.")
                    return

        password = input(" - PASSWORD = ").strip()

        if len(password) < 8:
            print(" ----------------------------------")
            print("\n -----------------------------------")
            print(" - Password tidak valid. Coba lagi.")
            print(" -----------------------------------")
            return

        decrypt_files(input_folder, output_folder, password, add_extension, file_extension)

    else:
        print("\n -------------------------------")
        print(" Pilihan tidak valid. Coba lagi.")
        print(" -------------------------------")

if __name__ == "__main__":
    main_menu()
    input("\n Tekan 'Enter' untuk keluar...")