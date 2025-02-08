import os
import tkinter as tk
from PIL import Image, ImageTk

global cwd
cwd = os.getcwd()

def show_image(image_path):
    root = tk.Tk()
    root.title("Image Viewer")
    
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    
    label = tk.Label(root, image=img)
    label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    image_path = cwd + "\\ggpo.png"  # Change this to the path of your image
    show_image(image_path)
