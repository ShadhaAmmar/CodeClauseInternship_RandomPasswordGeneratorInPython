import tkinter as tk
import random
import string

def generate_password():
    pw_length = int(entry_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pw_length))
    password_text.delete(1.0, tk.END)  # Clear previous text
    password_text.insert(tk.END, password)
    result_label.config(text="Generated Password:")

def regenerate_password():
    generate_password()

root = tk.Tk()
root.geometry("350x200")
root.title("Random Password Generator")

title_frame = tk.Frame(root)
title_frame.pack()

title_label = tk.Label(title_frame, text="{Code Clause};", font=("arial", 14, "bold"), fg="turquoise")
title_label.pack()

subtitle_label = tk.Label(title_frame, text="Random Password Generator", font=("arial", 12, "bold"), fg="DodgerBlue")
subtitle_label.pack()

input_frame = tk.Frame(root)
input_frame.pack()

label_length = tk.Label(input_frame, text="Enter Password Length:")
label_length.pack(side=tk.LEFT)

entry_length = tk.Entry(input_frame)
entry_length.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="lightblue")
generate_button.pack()

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Generated Password:")
result_label.pack(side=tk.LEFT)

password_text = tk.Text(result_frame, height=1, width=15)
password_text.pack(side=tk.LEFT)

regenerate_button = tk.Button(root, text="Regenerate", command=regenerate_password, bg="lightblue")
regenerate_button.pack()

root.mainloop()
