import time
import pyautogui
from playsound import playsound  # Import playsound

for i in range(1000):
    pyautogui.hotkey('ctrl', 'f')  # Buka panel pencarian
    time.sleep(0.15)
    pyautogui.hotkey('ctrl', 'a')  # Seleksi semua teks di panel pencarian
    time.sleep(0.15)
    pyautogui.hotkey('backspace')  # Hapus teks
    time.sleep(0.15)
    pyautogui.write(" = ")  # Cari ~z~
    time.sleep(0.15)
    pyautogui.press('enter')  # Pindah ke hasil pencarian
    time.sleep(0.15)
    pyautogui.hotkey('shift', 'enter')  # Seleksi hasil
    time.sleep(0.15)
    pyautogui.press('esc')  # Tutup panel pencarian
    time.sleep(0.15)
    pyautogui.hotkey('shift', 'end')  # Blokir teks setelahnya
    time.sleep(0.15)
    pyautogui.press('q')  # Shortcut untuk penerjemah
    time.sleep(0.15)

print("Semua file berhasil diproses.")
playsound(r"C:\Users\Aang Solihin\Downloads\Automatic\Where We Started feat Jex.mp3")  # Ganti dengan path file MP3 Anda