import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import subprocess

def close_video():
    cv2.destroyAllWindows()

def validate_selection(event):
    selected_value = selected_model.get()
    if selected_value == "Select Steps...":
        messagebox.showwarning("Warning", "Please choose a valid option.")

root = tk.Tk()
root.title("Bot Runner")
root.geometry("800x650")

icon_path = os.path.join("D:\\bot", "icon.ico")
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

models = ["Select Steps...", "50k", "1 Lakh", "2 Lakh"]
selected_model = tk.StringVar(value=models[0])

bg_image = Image.open("D:\\bot\\background.jpg")
background_photo = ImageTk.PhotoImage(bg_image)
alpha = 0.5

bg_image.putalpha(int(255 * alpha))
bg_image = bg_image.resize((800, 650), Image.LANCZOS)
background_image = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

heading_label = tk.Label(root, text="SuperMarioBros Game Bot", font=("Comic Sans MS", 40))
heading_label.place(relx=0.5, rely=0.1, anchor="n")

# Create a frame to group "Training Steps" label and dropdown
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.45, anchor="center")

training_label = tk.Label(frame, text="Training Steps :", font=("Cascadia Code Light", 14))
training_label.grid(row=0, column=0, padx=(0, 0))

model_dropdown = ttk.Combobox(frame, textvariable=selected_model, values=models)
model_dropdown.grid(row=0, column=1)
model_dropdown.bind("<<ComboboxSelected>>", validate_selection)




def open_py_file():
                 cmd = [
                  "jupyter", "nbconvert", 
                   "--to", "notebook", 
                   "--execute",
                   "Super_Mario_Bot (1).ipynb", 
                    "--output", "Super_Mario_Bot (1)_output.ipynb"
            ]
                 subprocess.run(cmd)
# open_py_file()

def play_video():
    model = selected_model.get()

    if model == "Select Steps...":
        messagebox.showwarning("Warning", "Please choose a valid option.")
    else:
        if model == "1 Lakh":
            # video_path = "D:\\bot\\1Lakh.mp4"
             open_py_file()
            
            
        elif model == "50k":
            video_path = "video_model_2.mp4"
        elif model == "2 Lakh":
            video_path = "2lk_steps.mp4"

        # cap = cv2.VideoCapture(video_path)
        # while True:
        #     ret, frame = cap.read()
        #     if not ret:
        #         break
        #     cv2.imshow("Video Player", frame)
        #     if cv2.waitKey(25) & 0xFF == 27:  
        #         break
        # cap.release()
        # cv2.destroyAllWindows()

play_button = tk.Button(root, text="Run Game", command=play_video)
play_button.place(relx=0.5, rely=0.6, anchor="center")

def on_closing():
    cv2.destroyAllWindows()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
