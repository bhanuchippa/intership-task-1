# Quick Start Guide

Get the Decision Tree Iris Classifier running in minutes.

## 1. Install Python

Make sure Python 3.9 or newer is installed.

- Windows: download from https://www.python.org/downloads/
- macOS / Linux: use the system package manager or install from the Python website

Verify installation:

```bash
python --version
```

## 2. Install Dependencies

Open a terminal in the `DecisionTreeProject` folder and install the required packages:

```bash
pip install -r requirements.txt
```

## 3. Run the App

Start the Flask server:

```bash
python app.py
```

Then visit:

```text
http://127.0.0.1:5000
```

## 4. Use the App

- Enter the four Iris flower measurements.
- Click `Predict Species`.
- View the predicted species, model accuracy, and generated visuals.

## Troubleshooting

- If you see `module not found`, confirm your virtual environment is active and dependencies are installed.
- If the page does not load, verify the server is running and the browser is pointing to `http://127.0.0.1:5000`.
- If the app cannot write images, ensure the `outputs/` folder exists and has write permission.

## Notes

- The first launch automatically trains the model and generates the output images.
- The application is designed to run on Windows, macOS, and Linux.
