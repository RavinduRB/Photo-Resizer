import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
def resize_image():
try:
# Get the selected image file path
image_path = file_path.get()
# Open the image file
image = Image.open(image_path)
# Get the desired height and width
new_height = int(entry_height.get())
new_width = int(entry_width.get())
# Resize the image
resized_image = image.resize((new_width, new_height),
                             Image.LANCZOS)
# Display the resized image
resized_image.thumbnail((300, 300))
resized_photo = ImageTk.PhotoImage(resized_image)
label_resized.config(image=resized_photo)
label_resized.image = resized_photo
# Display actual height and width of the resized image
resized_width, resized_height = resized_image.size
label_resized_size.config(text=f" Resized Image Size:
{resized_width}
x
{resized_height}
pixels
")
except Exception as e:
# Show error if any
status_label.config(text="Error: " + str(e))


def browse_file():
    # Open a file dialog to select an image file
    file_path.set(filedialog.askopenfilename())
    # Load and display the selected image
    image_path = file_path.get()
    if image_path:
        image = Image.open(image_path)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)
    label_selected_image.config(image=photo)
    label_selected_image.image = photo
    # Display actual height and width of the selected image
    image_width, image_height = image.size
    status_label.config(text=f" Original Image Size:
    {image_width}
    x
    {image_height}
    pixels
    ")
    # Create the main window
    root = tk.Tk()
    root.title("Image Resizer")
    # Variables
    file_path = tk.StringVar()
    # Create Label for Project title
    # Apply font style to title labe
    font_bold = ("Helvetica", 18, "bold")
    label_title = tk.Label(root, text="Image Resizer")
    label_title.config(fg="white", bg="Navy Blue", font=font_bold)
    label_title.grid(row=0, columnspan=2, padx=5, pady=5)
    # Create Label for Project title
    # Apply font style to title label
    font_bold = ("Calibri", 15, "bold")
    label_title = tk.Label(root, text="Easily Resize Image Offline for free")
    label_title.config(fg="Navy Blue", font=font_bold)
    label_title.grid(row=1, columnspan=2, padx=5, pady=5)
    # Widgets
    # Create label and place it on window layout
    label_select = tk.Label(root, text="Select Image:")
    label_select.grid(row=2, column=0, padx=5, pady=5)
    # Create browse button
    btn_browse = tk.Button(root, text="Browse", command=browse_file)
    btn_browse.grid(row=2, column=1, padx=5, pady=5)
    # Create status label
    status_label = tk.Label(root, text="", fg="green")
    status_label.grid(row=4, columnspan=2, padx=5, pady=5)
    # Create label to show selected image on form
    label_selected_image = tk.Label(root)
    label_selected_image.grid(row=2, columnspan=2, padx=5, pady=5)
    # Create width label and its entry widget
    label_width = tk.Label(root, text="Width (px):")
    label_width.grid(row=5, column=0, padx=5, pady=5)
    entry_width = tk.Entry(root)
    entry_width.grid(row=5, column=1, padx=5, pady=5)
    # Create height label and its entry widget
    label_height = tk.Label(root, text="Height (px):")
    label_height.grid(row=6, column=0, padx=5, pady=5)
    entry_height = tk.Entry(root)
    entry_height.grid(row=6, column=1, padx=5, pady=5)
    # Create resize button
    btn_resize = tk.Button(root, text="Resize", command=resize_image)
    btn_resize.grid(row=7, columnspan=2, padx=5, pady=5)
    # Create label to show resized image
    label_resized_image = tk.Label(root, text="", fg="green")
    label_resized_image.grid(row=6, columnspan=2, padx=5, pady=5)
    label_resized = tk.Label(root)
    label_resized.grid(row=9, columnspan=2, padx=5, pady=5)
    # Create label to show resized image size
label_resized_size = tk.Label(root, text="", fg="green")
label_resized_size.grid(row=10, columnspan=2, padx=5, pady=5)
# Start the main event loop
root.mainloop()