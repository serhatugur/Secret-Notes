from tkinter import *
import base64
from tkinter import messagebox

#Window
root = Tk()
root.title("Secret Notes")
root.iconbitmap("user.ico")
root.minsize(width=600, height=700)
root.maxsize(width=600, height=700)


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

#NotesToSave
def save_and_encrypt_note():
    title = entry1.get()
    message = text1.get("1.0",END)
    master_secret = entry2.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
            messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        message_encrypted = encode(master_secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        finally:
            entry1.delete(0, END)
            entry2.delete(0, END)
            text1.delete("1.0",END)

#DecryptNotes
def decrypt_note():
    message_encrypted = text1.get("1.0", END)
    master_secret = entry2.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            text1.delete("1.0", END)
            text1.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")





#label1
label1 = Label(root, text="Enter Your Title", font =("Helvetica 12 bold"))
label1.pack()
label1.place(x=228, y=190)
#entry1
entry1 = Entry(root, width=20)
entry1.pack()
entry1.place(x=228, y=220)

#label2
label2 = Label(root, text="Encrypt/Decrypt Text", font=("Helvetica 12 bold"))
label2.pack()
label2.place(x=208, y=255)
#text
text1 = Text(root, height=10, width=50)
text1.pack()
text1.place(x=95, y=280)

#label3
label3 = Label(root, text="Enter Master Key", font=("Helvetica 12 bold"))
label3.pack()
label3.place(x=220, y=450)
#entry2
entry2 = Entry(root, width=55, show="*")
entry2.pack()
entry2.place(x=130, y=480)

#button1
button1 = Button(text="Save & Encrypt", font=("Helvetica 10 bold"), command=save_and_encrypt_note)
button1.pack()
button1.place(x=221, y=510)
button1.config(width=15)

#button2
button2 = Button(text="Decrypt", font=("Helvetica 8 bold"), command=decrypt_note)
button2.pack()
button2.place(x=246, y=550)
button2.config(width=10)

#Photo
canvas = Canvas(height=150, width=150)
logo = PhotoImage(file="../SecretNotes/pngwng.png")
canvas.create_image(70,100,image=logo)
canvas.pack()










































root.mainloop()