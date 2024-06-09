import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import ImageClip, concatenate_videoclips
import os

def select_files():
    filetypes = (('Image files', '*.png;*.jpg;*.jpeg;*.gif'), ('All files', '*.*'))
    filenames = filedialog.askopenfilenames(title='Open files', filetypes=filetypes)
    
    if len(filenames) != 2:
        messagebox.showerror("Error", "Please select exactly 2 files.")
        return

    global selected_filenames
    selected_filenames = filenames

def create_gif():
    if len(selected_filenames) != 2:
        messagebox.showerror("Error", "Please select exactly 2 files.")
        return
    
    try:
        duration_per_image = 500  # Duration each image is displayed in seconds
        clips = [ImageClip(filename).set_duration(duration_per_image) for filename in selected_filenames]
        final_clip = concatenate_videoclips(clips, method="compose")
        output_path = os.path.join(os.path.dirname(__file__), 'output.gif')
        final_clip.write_gif(output_path, fps=1/duration_per_image)  # fps=1/duration_per_image to set each frame's duration
        messagebox.showinfo("Success", f"GIF created successfully! Saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create GIF: {e}")

window = tk.Tk()
window.title("GIF Creator by Rohan Mahajan")
window.configure(bg="#97DFFC")

icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)

selected_filenames = []

window_width = 420
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
window.minsize(420, 250)

title_label = tk.Label(window, text="GIF Creator by Rohan Mahajan", font=("Segoe UI Semibold", 16, "bold"), bg="#97DFFC", fg="black")
title_label.pack(pady=10)
instruction_label = tk.Label(window, text="Select 2 image files to create a GIF", font=("Segoe UI Semibold", 12), bg="#97DFFC", fg="black")
instruction_label.pack(pady=10)
select_button = tk.Button(window, text="Select Files", command=select_files, bg="#858AE3", fg="white", font=("Segoe UI Semibold", 12))
select_button.pack(pady=5, padx=10)
create_button = tk.Button(window, text="Create GIF", command=create_gif, bg="#613DC1", fg="white", font=("Segoe UI Semibold", 12))
create_button.pack(pady=20, padx=10)

window.mainloop()
