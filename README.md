# OCR with Tesseract

This is an OCR (Optical Character Recognition) application that uses **Tesseract** to extract text from images. It supports both **Bangla** and **English** languages for text extraction.

## Features

- Select an image to extract text.
- Supports Bangla (`ben`) and English (`eng`) languages.
- Copy extracted text to the clipboard.
- Text output is displayed in a text box with Bangla font support.

---

## Requirements

### Software

1. **Python 3.x**: This program is developed with Python 3. Ensure that you have it installed on your system.
2. **Tesseract OCR**: The core OCR engine that processes the images.
3. **Pillow**: Python library to work with images.
4. **Tkinter**: Python library for the graphical user interface (GUI).

### System Requirements

- **Linux (Debian-based systems such as Ubuntu)**

---

## Installation Steps

### 1. Install Tesseract OCR

You need to install **Tesseract** and language packs on your system.

#### On Ubuntu/Debian-based systems:

```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben
