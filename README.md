# image2text
# Rupom Image to Text

This is an OCR (Optical Character Recognition) application that uses Tesseract to extract text from images. It supports both Bangla and English languages for text extraction.

# Features
Select an image to extract text.
Supports Bangla (ben) and English (eng) languages.
Copy extracted text to the clipboard.
Text output is displayed in a text box with Bangla font support.

# Requirements 

Software
Python 3.x: This program is developed with Python 3. Ensure that you have it installed on your system.
Tesseract OCR: The core OCR engine that processes the images.
Pillow: Python library to work with images.
Tkinter: Python library for the graphical user interface (GUI).
System Requirements
Linux (Debian-based systems such as Ubuntu)
Installation Steps
1. Install Tesseract OCR
You need to install Tesseract and language packs on your system.

On Ubuntu/Debian-based systems:
bash
Copy code
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben
This installs the necessary OCR software and the English and Bangla language packs. You can add other language packs by replacing eng and ben with other language codes.

2. Install Python and Dependencies
Ensure you have Python 3.x installed. You can install Python by running:

bash
Copy code
sudo apt install python3 python3-pip
Then, install the required Python packages by running:

bash
Copy code
pip3 install pillow tkinter
This will install:

Pillow: To handle image processing.
tkinter: To create the graphical user interface.
3. Download the Application
Download the program files or clone the repository.

If you cloned the repository, navigate to the project directory:

bash
Copy code
cd path_to_your_project
4. Run the Application
Once all dependencies are installed and Tesseract is set up, you can run the application:

bash
Copy code
python3 ocr_app.py
This will launch the application, where you can select an image file to extract text. The program will output the text extracted from the image in the text box.

How to Use
Select an Image: Click the "Select Image and Extract Text" button to choose an image file from your system.
Extract Text: The application will use Tesseract OCR to extract text from the selected image.
Copy to Clipboard: You can copy the extracted text to your clipboard by clicking the "Copy to Clipboard" button.
Language Selection: Use the dropdown to select between Bangla (ben) and English (eng) for text extraction. The default language is Bangla.
Troubleshooting
Common Issues
Tesseract is not found: Ensure that Tesseract is installed properly and available in your system's PATH. You can test it by running tesseract --version in the terminal.

Language not installed: If the selected language is not installed, you will receive an error message. Install the language using:

bash
Copy code
sudo apt install tesseract-ocr-{language_code}
For Bangla, the code is ben, and for English, the code is eng.

License
This project is licensed under the MIT License - see the LICENSE file for details.

