import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageResizer:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Image Resizer")
        
        # Variables
        self.file_path = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create Label for Project title
        font_bold = ("Helvetica", 18, "bold")
        label_title = tk.Label(self.root, text="Image Resizer")
        label_title.config(fg="white", bg="navy")
        label_title.config(font=font_bold)
        label_title.grid(row=0, columnspan=2, padx=5, pady=5)
        
        # Subtitle
        font_sub = ("Calibri", 15, "bold")
        subtitle = tk.Label(self.root, text="Easily Resize Image Offline for free")
        subtitle.config(fg="navy", font=font_sub)
        subtitle.grid(row=1, columnspan=2, padx=5, pady=5)
        
        # Image selection
        label_select = tk.Label(self.root, text="Select Image:")
        label_select.grid(row=2, column=0, padx=5, pady=5)
        
        btn_browse = tk.Button(self.root, text="Browse", command=self.browse_file)
        btn_browse.grid(row=2, column=1, padx=5, pady=5)
        
        # Status and image display
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.grid(row=4, columnspan=2, padx=5, pady=5)
        
        self.label_selected_image = tk.Label(self.root)
        self.label_selected_image.grid(row=3, columnspan=2, padx=5, pady=5)
        
        # Width and height inputs
        label_width = tk.Label(self.root, text="Width (px):")
        label_width.grid(row=5, column=0, padx=5, pady=5)
        self.entry_width = tk.Entry(self.root)
        self.entry_width.grid(row=5, column=1, padx=5, pady=5)
        
        label_height = tk.Label(self.root, text="Height (px):")
        label_height.grid(row=6, column=0, padx=5, pady=5)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=6, column=1, padx=5, pady=5)
        
        # Resize and Save buttons (side by side)
        btn_resize = tk.Button(self.root, text="Resize", command=self.resize_image)
        btn_resize.grid(row=7, column=0, padx=5, pady=5)
        
        # Add Save button next to Resize button
        self.btn_save = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.btn_save.grid(row=7, column=1, padx=5, pady=5)
        self.btn_save.config(state='disabled')  # Initially disabled
        
        # Resized image display
        self.label_resized = tk.Label(self.root)
        self.label_resized.grid(row=9, columnspan=2, padx=5, pady=5)
        
        self.label_resized_size = tk.Label(self.root, text="", fg="green")
        self.label_resized_size.grid(row=10, columnspan=2, padx=5, pady=5)
        
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
        
        if file_path:
            try:
                image = Image.open(file_path)
                image.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(image)
                self.label_selected_image.config(image=photo)
                self.label_selected_image.image = photo
                
                image_width, image_height = image.size
                self.status_label.config(
                    text=f"Original Image Size: {image_width} x {image_height} pixels"
                )
            except Exception as e:
                self.status_label.config(text=f"Error: {str(e)}")
    
    def resize_image(self):
        try:
            image_path = self.file_path.get()
            image = Image.open(image_path)
            
            new_height = int(self.entry_height.get())
            new_width = int(self.entry_width.get())
            
            self.resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Display the resized image
            display_image = self.resized_image.copy()
            display_image.thumbnail((300, 300))
            resized_photo = ImageTk.PhotoImage(display_image)
            self.label_resized.config(image=resized_photo)
            self.label_resized.image = resized_photo
            
            # Display actual height and width of the resized image
            resized_width, resized_height = self.resized_image.size
            self.label_resized_size.config(
                text=f"Resized Image Size: {resized_width} x {resized_height} pixels"
            )
            
            # Enable save button
            self.btn_save.config(state='normal')
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            self.btn_save.config(state='disabled')
    
    def save_image(self):
        try:
            if not hasattr(self, 'resized_image'):
                raise Exception("No image to save")
                
            file_types = [
                ('PNG files', '*.png'),
                ('JPEG files', '*.jpg;*.jpeg'),
                ('All files', '*.*')
            ]
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=file_types
            )
            
            if save_path:
                self.resized_image.save(save_path)
                self.status_label.config(
                    text=f"Image saved successfully to: {save_path}"
                )
        except Exception as e:
            self.status_label.config(text=f"Error saving image: {str(e)}")

if __name__ == "__main__":
    app = ImageResizer()
    app.root.mainloop()
