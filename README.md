# Flask Sample Project 🚀

Welcome to the **Flask Sample Project**! This is a fun and simple project to demonstrate a Flask-based API for managing products and carts. 🛒

## Features ✨
- Manage products (CRUD operations)
- Manage carts (CRUD operations)
- Fully tested with `unittest`

## Setting Up a Virtual Environment 🐍

Before installing dependencies, it's recommended to set up a virtual environment to isolate your project:

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Once activated, you can proceed to install the dependencies as described in the installation steps.

## Installation 🛠️

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd flask-sample
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application ▶️
1. Start the Flask server:
   ```bash
   python api.py
   ```
2. Access the API at `http://127.0.0.1:5000`

## Running Tests 🧪
Run the tests to ensure everything is working:
```bash
python -m unittest discover
```

## Contributing 🤝
We welcome contributions! Please see the `CONTRIBUTING.md` file for guidelines.

## License 📜
This project is licensed under the MIT License. See the `LICENSE` file for details.