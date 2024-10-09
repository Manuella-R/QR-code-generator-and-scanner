# QR Code Generator and Scanner

This project provides two functionalities in separate GUI applications built using **Tkinter** and **ttkinter**:
1. **QR Code Scanner**: Upload a QR code image and view the encoded description.
2. **QR Code Generator**: Input details to generate a QR code and download the QR image.

## Features

### 1. QR Code Scanner
- **Upload an Image**: Users can upload an image containing a QR code.
- **Scan and Decode**: The QR code is scanned, and the encoded data is displayed.
- **Clear Interface**: The GUI is clean, with a blue button allowing users to upload images, and a description of the scanned data is shown below.
  
Example:
![QR Code Scanner](./path-to-QR-Code-Scanner.png)

### 2. QR Code Generator
- **Enter QR Code Title and Description**: Users input a title and a description that will be encoded in the QR code.
- **Generate QR Code**: On clicking the “Generate QR Code” button, a QR code is displayed based on the provided description.
- **Download QR Code**: A button is provided to download the generated QR code as an image file.
- **Simple Interface**: The layout is straightforward, with fields for input, a “Generate QR Code” button, and a preview of the generated QR code, followed by a download option.

Example:
![QR Code Generator](./path-to-QR-Code-Generator.png)

## Requirements
- Python 3.x
- `Tkinter` (built-in with Python)
- `Pillow` for image handling
- `Pyzbar` for QR code decoding

You can install the required libraries using:
```bash
pip install tkinter pillow pyzbar
```

## How to Run
1. **QR Code Scanner**:
    - Run the `qr_code_scanner.py` script.
    - Upload a QR code image and view its decoded description.

2. **QR Code Generator**:
    - Run the `qr_code_generator.py` script.

