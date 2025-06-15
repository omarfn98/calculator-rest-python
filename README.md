# Calculator REST Service (Python Flask)

This project implements a simple RESTful web service using **Python Flask** that performs **addition on a comma-separated list of numbers** and returns the result in **JSON format**.

The service is designed to be **safe, resilient**, and handles a variety of inputs gracefully. A **unit test suite** is also included to verify the implementation logic.

---
# Create and activate virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

# Install dependencies
```bash
pip install -r requirements.txt
```

## Setup
```bash
pip install -r requirements.txt
```

## Run the App
```bash
python app.py
```

## Example Usage
```
curl "http://127.0.0.1:5000/calculator/add?operands=1,2.5,3"
Response: {"sum": 6.5}
```

## Run Tests
```bash
python -m unittest test_app.py
```
