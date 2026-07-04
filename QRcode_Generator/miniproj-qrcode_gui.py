import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import webbrowser

def generate_qr():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter a link or text.")
        return

    filename = "generated_qr.png"

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2E86C1", back_color="white")
    img.save(filename)

    # Load and show image in GUI
    qr_img = Image.open(filename)
    qr_img = qr_img.resize((220, 220), Image.Resampling.LANCZOS)  # FIXED
    img_tk = ImageTk.PhotoImage(qr_img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    qr_label.pack(pady=(10, 5))

    download_link.config(text="📥 Click here to open/download QR Code", fg="#117A65", cursor="hand2")
    download_link.pack()

def open_qr():
    filepath = os.path.abspath("generated_qr.png")
    if os.path.exists(filepath):
        webbrowser.open(f"file://{filepath}")
    else:
        messagebox.showerror("File Error", "QR Code file not found.")

# UI setup
root = Tk()
root.title("QR Code Generator")
root.geometry("420x580")
root.configure(bg="#ECF0F1")

Label(root, text="QR Code Generator", font=("Helvetica", 22, "bold"), fg="#1A5276", bg="#ECF0F1").pack(pady=20)

entry = Entry(root, width=35, font=("Arial", 14), bd=2, relief=SOLID, justify='center')
entry.pack(pady=10)
entry.focus()

Button(root, text="Generate QR Code", font=("Arial", 14), bg="#1F618D", fg="white", padx=10, pady=6, command=generate_qr).pack(pady=15)

qr_label = Label(root, bg="#ECF0F1")
qr_label.pack_forget()

download_link = Label(root, text="", font=("Arial", 12, "underline"), bg="#ECF0F1")
download_link.bind("<Button-1>", lambda e: open_qr())
download_link.pack_forget()

Label(root, text="Made with 💙 by Sukanya", font=("Arial", 10), bg="#ECF0F1", fg="#7D7D7D").pack(side=BOTTOM, pady=10)

root.mainloop()
