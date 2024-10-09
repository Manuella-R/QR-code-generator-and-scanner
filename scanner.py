import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
from ttkbootstrap import Style

def upload_qr_code():
    # Ask the user to upload an image file
    file_path = filedialog.askopenfilename(
        title="Select QR Code Image", 
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    
    if not file_path:
        return

    try:
        # Open the image file
        img = Image.open(file_path)
        
        # Decode the QR code
        qr_codes = decode(img)
        if qr_codes:
            qr_data = qr_codes[0].data.decode('utf-8')  # Get the data from the first QR code
            qr_type = qr_codes[0].type
            result_label.config(text=f"QR Code Data:\n {qr_data}")
        else:
            result_label.config(text="No QR Code found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open or decode the image: {e}")

# Create the main window
root = tk.Tk()
root.title("QR Code Scanner")
root.geometry("400x400")
root.configure(bg="pink")
style = Style(theme="superhero")

# Create and place widgets
upload_button = ttk.Button(root, text="Upload QR Code Image", command=upload_qr_code)
upload_button.pack(pady=20)
style.configure('TButton', font=('TkDefaultFont', 16), foreground="white")

result_label = ttk.Label(root, text="Upload an image to scan the QR code.", wraplength=300)
result_label.pack(pady=20)
style.configure('TLabel', font=('TkDefaultFont', 16), foreground="white")

# Start the Tkinter event loop
root.mainloop()
