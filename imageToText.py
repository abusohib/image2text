import tkinter as tk
from tkinter import filedialog, messagebox, font
import os
import subprocess

def validate_tesseract():
    """Validate if Tesseract is installed and the selected language is available."""
    try:
        # Check if Tesseract is installed
        result = subprocess.run(
            ["tesseract", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            raise FileNotFoundError("Tesseract OCR not found.")
        
        # Check available languages
        result = subprocess.run(
            ["tesseract", "--list-langs"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            raise Exception("Unable to retrieve language list from Tesseract.")
        
        # Parse available languages
        available_languages = result.stdout.splitlines()[1:]  # Ignore the first line
        if language_var.get() not in available_languages:
            messagebox.showerror(
                "Language Missing",
                f"The selected language '{language_var.get()}' is not installed.\n"
                "Please install it using:\n"
                f"sudo apt install tesseract-ocr-{language_var.get()}"
            )
            return False

        return True
    except FileNotFoundError as e:
        messagebox.showerror("Error", "Tesseract is not installed. Please install it first.")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"Error validating Tesseract:\n{e}")
        return False

def extract_text():
    """Extract text from the selected image."""
    if not validate_tesseract():
        return

    # Select the image file
    image_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.tiff *.bmp")]
    )
    if not image_path:
        return
    
    # Define output text file
    output_path = os.path.splitext(image_path)[0] + "_output.txt"
    
    # Get the selected language
    selected_language = language_var.get()

    try:
        # Run Tesseract
        result = subprocess.run(
            ["tesseract", image_path, output_path.replace(".txt", ""), "-l", selected_language],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr.strip())

        # Read and display extracted text
        with open(output_path, "r", encoding="utf-8") as file:
            extracted_text = file.read()
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, extracted_text)
        messagebox.showinfo("Success", f"Text extracted successfully!\nSaved at: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text:\n{e}")

def copy_to_clipboard():
    """Copy the text output to the clipboard."""
    text = text_output.get("1.0", tk.END).strip()
    if text:
        app.clipboard_clear()
        app.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No text to copy!")

# Create main application window
app = tk.Tk()
app.title("OCR with Tesseract")
app.geometry("800x600")

# Language selection dropdown
language_var = tk.StringVar(value="ben")
language_dropdown = tk.OptionMenu(app, language_var, "ben", "eng")
language_dropdown.pack(pady=5)

# Label
label = tk.Label(app, text="Select an image to extract text using Tesseract OCR", font=("Arial", 14))
label.pack(pady=10)

# Button frame
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

# Select and extract text button
browse_button = tk.Button(button_frame, text="Select Image and Extract Text", command=extract_text, bg="blue", fg="white", font=("Arial", 12))
browse_button.pack(side=tk.LEFT, padx=5)

# Copy to clipboard button
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white", font=("Arial", 12))
copy_button.pack(side=tk.LEFT, padx=5)

# Text output box
bangla_font = font.Font(family="SolaimanLipi", size=12)
text_output = tk.Text(app, wrap=tk.WORD, font=bangla_font, height=20)
text_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Start the application
app.mainloop()
