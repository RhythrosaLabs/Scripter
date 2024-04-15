# GPT Scritper

This Python script utilizes OpenAI's GPT models to generate content in various file formats based on user input. The script provides a graphical user interface (GUI) where users can input their request, select the desired output format, and generate content accordingly.

## Features

- Supports a wide range of file formats including Python, XML, HTML, JSON, Markdown, CSV, YAML, JavaScript, Java, C++, and more.
- Provides a user-friendly interface for inputting requests and selecting output formats.
- Generates content using OpenAI's powerful GPT models.
- Saves the generated content to a file with the appropriate extension.

## Installation

1. Clone the repository.

2. Navigate to the cloned directory.

3. Install the required dependencies:
pip install openai tkinter


## Usage

1. Run the script:
python script_name.py

vbnet
Copy code

2. Enter your request in the input text box.
3. Select the desired output format from the dropdown menu.
4. Click on the "Generate" button.
5. The generated content will be displayed in the output box and saved to a file.

## How It Works

1. **Input Request**: Users input their request in the text box provided.
2. **Select Output Format**: Users select the desired output format from the dropdown menu.
3. **Generate Content**: Upon clicking the "Generate" button, the script constructs a prompt specific to the chosen format and calls OpenAI's API to generate content.
4. **Save Content**: The generated content is then saved to a file with the corresponding extension.

## Note

- Ensure you have a valid OpenAI API key for accessing the GPT models.
- Handle your API key securely to prevent unauthorized access.
- For extensive customization or integration, the script can be modified as needed.
- This project is licensed under the MIT License.
