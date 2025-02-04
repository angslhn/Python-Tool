import pyautogui
import keyboard

def paste_text():
    # Simulasi CTRL + V
    pyautogui.hotkey('ctrl', 'v')

# Mendeteksi F6 ditekan
keyboard.add_hotkey('F6', paste_text)

print("Tekan F6 untuk melakukan CTRL + V pada teks yang diblokir...")
keyboard.wait('esc')  # Tekan ESC untuk keluar dari program