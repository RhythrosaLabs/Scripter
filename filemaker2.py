import tkinter as tk
from tkinter import filedialog, Scrollbar
import openai
import json

# Read the API key from a JSON file
def read_api_key_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data['api_key']

# Use the function to get the API key
api_key_path = 'api_key.json'
openai.api_key = read_api_key_from_json(api_key_path)
import json

# Read the API key from a JSON file
def read_api_key_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data['api_key']

# Use the function to get the API key
api_key_path = 'api_key.json'
openai.api_key = read_api_key_from_json(api_key_path)

#====================================================================================================================
#==================================================================================================================== 

def create_file(filename, content):
    """Create a file with the given filename and content."""
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    """Read the content of a file with the given filename."""
    with open(filename, 'r') as f:
        return f.read()

def save_file_with_dialog(content):
    """Save the content to a file chosen through a file dialog."""
    file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path
    return None

#------------------------------------------------------------------------------------------------------------

def save_as_sheet_music():
    content = output_text.get("1.0", tk.END).strip()
    filepath = filedialog.asksaveasfilename(defaultextension=".ly", filetypes=[("LilyPond files", "*.ly"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'w') as f:
            f.write(content)
        output_text.insert(tk.END, f"\nFile saved to: {filepath}")

def save_as_midi():
    content = output_text.get("1.0", tk.END).strip()
    filepath = filedialog.asksaveasfilename(defaultextension=".abc", filetypes=[("ABC files", "*.abc"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'w') as f:
            f.write(content)
        output_text.insert(tk.END, f"\nFile saved to: {filepath}")

def save_as_svg():
    content = output_text.get("1.0", tk.END).strip()
    filepath = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'w') as f:
            f.write(content)
        output_text.insert(tk.END, f"\nFile saved to: {filepath}")
        
#------------------------------------------------------------------------------------------------------------

def call_openai_api(prompt):
    """Call OpenAI API with a given prompt and return the response."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def on_request():
    # Get request from the input_text widget
    request = input_text.get("1.0", tk.END).strip()
    
    # Get the selected file type
    file_type = selected_file_type.get()
    
    # Refine the prompt for OpenAI API based on selected file type
    if file_type == "MIDI":
        gpt_prompt = f"Generate ABC notation for a simple melody based on the theme: {request}."
    elif file_type == "Sheet Music":
        gpt_prompt = f"Generate LilyPond notation for a simple melody based on the theme: {request}."
    elif file_type == "Markdown":
        gpt_prompt = f"Generate a Markdown file that contains a {request}."
    elif file_type == "SVG":
        gpt_prompt = f"Generate an SVG file for a simple shape based on the theme: {request}."
    elif file_type == "HTML":
        gpt_prompt = f"Generate HTML code for a simple web page that displays {request}."
    elif file_type == "Python":
        gpt_prompt = f"Generate Python code that performs {request}."
    elif file_type == "Unity":
        gpt_prompt = f"Generate a Unity C# script that implements {request}."
    elif file_type == "Blender":
        gpt_prompt = f"Generate Python code for a Blender script that creates {request}."
    elif file_type == "Excel":
        gpt_prompt = f"Describe how to set up an Excel sheet for {request}."
    elif file_type == "Google Sheet":
        gpt_prompt = f"Describe how to set up a Google Sheet for {request}."
    elif file_type == "Google Doc":
        gpt_prompt = f"Describe how to set up a Google Doc for {request}."
    elif file_type == "C++":
        gpt_prompt = f"Generate C++ code that performs {request}."
    elif file_type == "Java":
        gpt_prompt = f"Generate Java code that performs {request}."
    elif file_type == "Sonic Pi":
        gpt_prompt = f"Generate Sonic Pi code for a tune based on {request}."
    elif file_type == "Arduino Sketch":
        gpt_prompt = f"Generate an Arduino sketch for {request}."
    elif file_type == "Jupyter Notebook":
        gpt_prompt = f"Generate Jupyter Notebook cells for data analysis on {request}."
    elif file_type == "After Effects Expressions":
        gpt_prompt = f"Generate Adobe After Effects expressions for {request}."
    elif file_type == "OBS Studio JSON":
        gpt_prompt = f"Generate OBS Studio scene JSON for {request}."
    elif file_type == "Lisp":
        gpt_prompt = f"Generate a Lisp function to accomplish {request}."
    elif file_type == "Perl":
        gpt_prompt = f"Generate a Perl script for {request}."
    elif file_type == "MATLAB":
        gpt_prompt = f"Generate MATLAB code for {request}."
    elif file_type == "LaTeX":
        gpt_prompt = f"Generate a LaTeX snippet for {request}."
    elif file_type == "YAML":
        gpt_prompt = f"Generate a YAML configuration for {request}."
    elif file_type == "SQL":
        gpt_prompt = f"Generate SQL queries to perform {request}."
    
    # Call OpenAI API
    response = call_openai_api(gpt_prompt)
    
    # Parse the response to determine file type and content
    lines = response.split('\n')
    generated_file_type = lines[0].split(":")[-1].strip().lower()
    content = '\n'.join(lines[1:])
    
    # Insert the content into output_text (the "notepad" area)
    output_text.delete("1.0", tk.END)  # Clear previous content
    output_text.insert(tk.END, content)  # Insert new content

def on_save():
    content = read_file("output.txt")
    filepath = save_file_with_dialog(content)
    output_label.config(text=f"File saved to: {filepath}")

def on_delete():
    delete_file("output.txt")
    output_label.config(text="File deleted.")

#====================================================================================================================
#==================================================================================================================== 

#====================================================================================================================
#==================================================================================================================== 


# Create the main tkinter window
root = tk.Tk()
root.title("GPT File Creator GUI")

# Make the window resizable
root.resizable(True, True)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create a Tkinter StringVar to hold the selected file type
selected_file_type = tk.StringVar(root)
selected_file_type.set("Markdown")  # default value

# Update the file_type_options list to include "SVG"
file_type_options = [
    "MIDI", "Sheet Music", "Markdown", "SVG",
    "HTML", "Python", "Unity", "Blender", 
    "Excel", "C++", "Java", "Sonic Pi",
    "XML", "JSON", "CSV", "Ruby",
    "Bash Script", "PowerShell Script", "R Script",
    "Kotlin", "Rust", "Dart", "Arduino Sketch",
    "Jupyter Notebook", "After Effects Expressions",
    "OBS Studio JSON", "Lisp", "Perl", "MATLAB",
    "LaTeX", "YAML", "SQL"
]
file_type_menu = tk.OptionMenu(root, selected_file_type, *file_type_options)
file_type_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

request_button = tk.Button(root, text="Generate", command=on_request)
request_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Create and pack the widgets for text entry
input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=1, columnspan=2, padx=10, pady=20, sticky="nsew")
input_text.insert(tk.END, "Enter your request here...")

# Create and pack the widgets for save file button
save_button = tk.Button(root, text="Save File", command=on_save)
save_button.grid(row=2, columnspan=2, padx=10, pady=10, sticky="ew")

# Create and pack the widgets for notepad
output_text = tk.Text(root, height=15, width=50)
output_text.grid(row=3, columnspan=2, padx=10, pady=20, sticky="nsew")
output_text.insert(tk.END, "Generated content will appear here...")

# Run the Tkinter event loop
root.mainloop()
