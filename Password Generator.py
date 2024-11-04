import tkinter as tk
import secrets
import string

def generate_password(length=8):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine character sets
    all_characters = letters + digits + special_characters
    
   

    # Generate password
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def on_generate():
    length = int(length_entry.get())
    password = generate_password(length)
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "8")

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
