# Decision Tree Iris Classifier

A beginner-friendly Flask project that trains and visualizes a Decision Tree model using the Iris dataset from Scikit-learn. This application predicts flower species based on four input measurements and displays model accuracy, confusion matrix, and decision tree visualization.

## Features

- Train a Decision Tree Classifier using the Iris dataset
- Predict Iris species from custom user input
- Display model accuracy in the UI
- Show the confusion matrix and decision tree visualization
- Responsive, modern dashboard design
- Instant prediction through AJAX POST requests
- Automatic model training and loading on server start

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- HTML / CSS / JavaScript

## Project Structure

```text
DecisionTreeProject/
├── app.py
├── model/
│   └── train_model.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── templates/
│   └── index.html
├── outputs/
│   ├── decision_tree.png
│   └── confusion_matrix.png
├── requirements.txt
├── README.md
├── QUICK_START.md
└── .gitignore
```

## Installation

1. Clone the repository or copy the project folder.
2. Open a terminal in the `DecisionTreeProject` folder.
3. Create a Python virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Locally

Start the Flask app with:

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:5000
```

## Expected Outputs

- A polished web interface with input fields for sepal and petal measurements
- Prediction result displayed instantly
- Model accuracy text shown on the dashboard
- Decision tree visualization image
- Confusion matrix image

## Screenshots

![App Screenshot](outputs/decision_tree.png)

> The image above is generated automatically when the app starts.

## Future Improvements

- Add support for saving user query history
- Provide probability scores for each species
- Add a dataset upload feature for custom data
- Support multiple model options (Random Forest, SVM)
- Add unit tests for backend endpoints and validation
