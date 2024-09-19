# Image to ASCII Converter

This project is a web application that converts images to ASCII art using FastAPI and Python. It features both a web interface and a command-line interface for converting images to ASCII representations.

## Features

- Web-based interface with a terminal-like UI
- Command-line interface for image conversion
- Supports various image formats
- Removes ANSI color codes from the output for better compatibility

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/image-to-ascii-converter.git
   cd image-to-ascii-converter
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Web Interface

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Use the terminal-like interface to convert images:
   - Type `help` for available commands
   - Use the `convert` command to select and convert an image

### Command-line Interface

Run the following command to use the CLI:
- `help`: Show available commands
- `convert`: Convert an image to ASCII. You will be prompted to enter the path to your image file.
- `clear`: Clear the terminal output

For example, to convert an image:

1. Run the CLI:
   ```
   python main.py cli
   ```
2. At the prompt, type:
   ```
   convert
   ```
3. When prompted, enter the path to your image file.

The ASCII art result will be displayed in the terminal.