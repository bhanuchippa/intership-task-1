import os
import pickle
from flask import Flask, render_template, request, jsonify, send_from_directory
from model.train_model import IrisModelPipeline

# Initialize Flask application with static and template folders
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load or train model automatically when the server starts
pipeline = IrisModelPipeline()
pipeline.setup()

# Home route renders the dashboard page
@app.route('/')
def index():
    return render_template(
        'index.html',
        accuracy=f"{pipeline.accuracy:.2f}%",
        species_names=pipeline.target_names,
        decision_tree_image='/outputs/decision_tree.png',
        confusion_matrix_image='/outputs/confusion_matrix.png'
    )

# Prediction API route accepts JSON payload and returns prediction details
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            raise ValueError('Invalid request payload. Use JSON format.')

        required = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        values = []

        for key in required:
            if key not in data:
                raise ValueError(f'Missing field: {key}')
            try:
                value = float(data[key])
            except (TypeError, ValueError):
                raise ValueError(f'Invalid value for {key}. Use numeric input.')
            values.append(value)

        prediction = pipeline.predict(values)

        return jsonify({
            'success': True,
            'predicted_species': prediction,
            'accuracy': f"{pipeline.accuracy:.2f}%",
            'message': 'Prediction generated successfully.'
        })

    except ValueError as error:
        return jsonify({'success': False, 'error': str(error)}), 400
    except Exception as error:
        return jsonify({'success': False, 'error': 'Server error. Please try again.'}), 500

# Serve generated output images from the outputs folder
@app.route('/outputs/<path:filename>')
def serve_output(filename):
    output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'outputs')
    return send_from_directory(output_dir, filename)

# Run the Flask server when the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
