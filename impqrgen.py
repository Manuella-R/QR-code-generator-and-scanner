import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import os
from ttkbootstrap import Style

# Function to generate QR code
def generate_qr():
    title = title_entry.get()
    desc = desc_entry.get()
    if not title or not desc:
        messagebox.showwarning("Input Error", "Please fill both title and description.")
        return
    
    # Create QR code
    qr_img = qrcode.make(desc)
    
    # Save image temporarily
    temp_path = f"{title}.png"
    qr_img.save(temp_path)
    
    # Display the QR code in the window
    img = Image.open(temp_path)
    img = img.resize((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    
    # Enable the download button
    download_button.config(state=tk.NORMAL)
    global saved_image
    saved_image = temp_path

# Function to download the QR code
def download_qr():
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        os.rename(saved_image, save_path)
        messagebox.showinfo("Saved", f"QR code saved as {save_path}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x600")
root.configure(bg="pink")
style = Style(theme="cyborg")


# Title label and entry
tk.Label(root, text="QR Code Title:").pack(pady=30)
title_entry = tk.Entry(root)
title_entry.pack()

# Description label and entry
tk.Label(root, text="QR Code Description:").pack(pady=30)
desc_entry = tk.Entry(root)
desc_entry.pack()

# Generate QR code button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=40)
style.configure('TButton', font=('TkDefaultFont', 16), foreground="red")

# QR Code display label
qr_label = tk.Label(root)
qr_label.pack(pady=30)

# Download button (disabled until QR is generated)
download_button = tk.Button(root, text="Download QR Code", state=tk.DISABLED, command=download_qr)
download_button.pack(pady=30)

# Start the Tkinter event loop
root.mainloop()
