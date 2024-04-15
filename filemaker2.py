import tkinter as tk
from tkinter import filedialog, messagebox
import openai
import os
import threading
import json

def load_or_request_api_key():
    root = tk.Tk()
    root.withdraw()
    api_key_path = 'api_key.json'
    if os.path.exists(api_key_path):
        with open(api_key_path, 'r') as file:
            data = json.load(file)
            return data.get('api_key', '')
    api_key = simpledialog.askstring("API Key", "Please enter your OpenAI API key:", parent=root)
    if api_key:
        with open(api_key_path, 'w') as file:
            json.dump({'api_key': api_key}, file)
    root.destroy()
    return api_key

openai.api_key = load_or_request_api_key()

def call_openai_api(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Respond only in the specified format."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def async_call_openai_api(prompt, callback):
    thread = threading.Thread(target=lambda: callback(call_openai_api(prompt)))
    thread.start()

def on_response_received(response):
    file_extension = file_type_to_extension[selected_file_type.get()]
    filename = f'output{file_extension}'
    with open(filename, 'w') as file:
        file.write(response)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"File generated: {os.path.abspath(filename)}")

def on_request():
    file_type = selected_file_type.get()
    prompt = f"Generate content in {file_type} format: " + input_text.get("1.0", tk.END).strip()
    if prompt:
        async_call_openai_api(prompt, on_response_received)
    else:
        messagebox.showerror("Error", "Please enter a valid request.")

root = tk.Tk()
root.title("GPT Content Generator in Specific Formats")

selected_file_type = tk.StringVar(root)
selected_file_type.set("Python")  # default selection
file_type_options = [
    "Python", "XML", "HTML", "JSON", "Markdown", "CSV", "YAML", "JavaScript",
    "Java", "C++", "C#", "LaTeX", "SQL", "PHP", "INI", "R", "Plain Text", "Rich Text Format"
]
file_type_to_extension = {
    "Python": ".py", "XML": ".xml", "HTML": ".html", "JSON": ".json", "Markdown": ".md",
    "CSV": ".csv", "YAML": ".yaml", "JavaScript": ".js", "Java": ".java", "C++": ".cpp",
    "C#": ".cs", "LaTeX": ".tex", "SQL": ".sql", "PHP": ".php", "INI": ".ini", "R": ".r",
    "Plain Text": ".txt", "Rich Text Format": ".rtf"
}
file_type_menu = tk.OptionMenu(root, selected_file_type, *file_type_options)
file_type_menu.grid(row=0, column=0, padx=10, pady=10)

input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=1, column=0, padx=10, pady=10)
input_text.insert(tk.END, "Enter your request here...")

send_button = tk.Button(root, text="Generate", command=on_request)
send_button.grid(row=1, column=1, padx=10, pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
