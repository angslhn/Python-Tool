import os
import re
from googletrans import Translator

def translate_text(text, translator):
    """Menerjemahkan teks menggunakan googletrans."""
    try:
        translated = translator.translate(text, src='en', dest='id')
        return translated.text
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text  # Jika gagal, kembalikan teks asli

def process_file(file_path, output_folder, translator):
    """Memproses file tunggal untuk menerjemahkan percakapan."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    for line in lines:
        match = re.search(r'(~z~)(.+)', line)  # Cari teks setelah ~z~
        if match:
            prefix = match.group(1)  # Simpan ~z~
            original_text = match.group(2)  # Teks asli setelah ~z~
            
            # Terjemahkan teks percakapan
            translated_text = translate_text(original_text, translator)
            
            # Format huruf besar setelah tanda baca
            translated_text = re.sub(r'(?<=[.!?])(\s*)(\w)', lambda m: ' ' + m.group(2).upper(), translated_text)
            
            # Gabungkan kembali dengan format aslinya
            line = line.replace(original_text, translated_text)

        translated_lines.append(line)

    # Tulis hasil ke folder output
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, os.path.basename(file_path))
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)

def main():
    input_folder = r"C:\Users\Aang Solihin\Downloads\Compressed\Bahasa Inggris"  # Folder tempat file .oxt
    output_folder = r"C:\Users\Aang Solihin\Downloads\Compressed\Bahasa Indonesia"  # Folder untuk file hasil terjemahan
    translator = Translator()  # Inisialisasi Google Translator

    # Proses semua file di folder input
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.oxt'):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing {file_name}...")
            process_file(file_path, output_folder, translator)
            print(f"Translated {file_name} saved to {output_folder}.")

if __name__ == "__main__":
    main()
