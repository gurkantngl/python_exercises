import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0", tk.END)
    master_secret = master_secret_input.get()
    
    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info.")
    
    else:
        #encryption
        encrypted_message = encode(master_secret, message)
        
        try:        
            with open("my_secret.txt", "a") as file:
                file.write(f"\n{title}\n{encrypted_message}")
        except FileNotFoundError:
            with open("my_secret.txt", "w") as file:
                file.write(f"\n{title}\n{encrypted_message}")
        finally:
            title_entry.delete(0,tk.END)
            master_secret_input.delete(0, tk.END)
            input_text.delete("1.0", tk.END)
        
def decrypt_notes():
    key = master_secret_input.get()
    
    with open("my_secret.txt", "r") as file:
        text = file.read()
        
# window options
FONT = ("Verdena", 12, "bold")

window = tk.Tk()
window.title("Secret Notes")
#window.configure(bg = "#E5E3E3")
window.config(padx=30, pady=30)



#UI
title_info_label = tk.Label(window, text= "Enter Your Title", font= FONT)
title_info_label.pack()

title_entry = tk.Entry(width=30)
title_entry.pack()

input_info_label = tk.Label(window, text= "Enter your secret", font= FONT)
input_info_label.pack()

input_text = tk.Text(width=50, height=25)
input_text.pack()

master_secret_label = tk.Label(text= "Enter master key",font= FONT)
master_secret_label.pack()


master_secret_input = tk.Entry(width= 30)
master_secret_input.pack()


save_button = tk.Button(text= "Save & Encrypt", command= save_and_encrypt_notes)
save_button.pack()

decrypt_button = tk.Button(text= "Decrypt", command= decrypt_notes)
decrypt_button.pack()

window.mainloop()