# Password Generator

A secure and user-friendly password generator application built with Python and Tkinter. This application allows users to generate strong passwords with customizable options.

## Author

**Fernando Valente**
- Website: [fernandovalente.com.br](https://fernandovalente.com.br)

## Features

- Generate passwords with customizable length
- Options to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Special characters (!@#$%^&*)
  - Numbers (0-9)
- Copy password to clipboard functionality
- Modern and intuitive user interface
- Minimum password length validation
- Error handling and user feedback

## Project Structure

- `password_generator.py`: Main application file containing both the GUI and password generation logic
- `test_password_generator.py`: Test suite for the password generation logic
- `requirements.txt`: Project dependencies
- `password_generator.spec`: PyInstaller specification file for creating the executable

## Dependencies

The project uses the following packages:

- `pyperclip`: For clipboard operations (copying passwords)
- `pytest`: For running the test suite
- `pyinstaller`: For creating the Windows executable

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd password-generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Mode

To run the application in development mode:

```bash
python password_generator.py
```

### Running Tests

To run the test suite:

```bash
pytest test_password_generator.py -v
```

## Creating the Executable

To create a standalone Windows executable:

1. Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

2. Build the executable:
```bash
pyinstaller password_generator.spec
```

3. The executable will be created in the `dist` folder as `Password Generator.exe`

## Project Architecture

The project follows a simple but effective architecture:

- `PasswordGeneratorLogic`: Handles the core password generation functionality
  - Validates input parameters
  - Generates secure random passwords
  - Manages password requirements

- `PasswordGenerator`: Manages the GUI and user interaction
  - Creates and manages the Tkinter interface
  - Handles user input
  - Provides feedback through message boxes
  - Integrates with the password generation logic

## Security Features

- Minimum password length of 4 characters
- At least one character type must be selected
- Uses Python's secure random number generator
- No password storage or logging

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Python Tkinter documentation
- PyInstaller documentation
- Python string and random modules documentation 