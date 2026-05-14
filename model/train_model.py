import os
import pickle
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix


class IrisModelPipeline:
    """Train and manage a Decision Tree model for the Iris dataset."""

    def __init__(self):
        self.package_dir = os.path.dirname(__file__)
        self.project_dir = os.path.abspath(os.path.join(self.package_dir, os.pardir))
        self.model_path = os.path.join(self.package_dir, 'decision_tree_model.pkl')
        self.output_dir = os.path.join(self.project_dir, 'outputs')
        self.feature_names = None
        self.target_names = None
        self.model = None
        self.accuracy = 0.0
        self.confusion_matrix = None
        self._ensure_directories()

    def _ensure_directories(self):
        os.makedirs(self.output_dir, exist_ok=True)

    def setup(self):
        """Train or load the model, then generate evaluation data and visuals."""
        iris = load_iris()
        self.feature_names = [name.replace(' (cm)', '').title() for name in iris.feature_names]
        self.target_names = list(iris.target_names)

        X = pd.DataFrame(iris.data, columns=self.feature_names)
        y = iris.target

        if os.path.exists(self.model_path):
            self._load_model()
        else:
            self._train_model(X, y)

        self._evaluate_model(X, y)
        self._save_visualizations()

    def _train_model(self, X, y):
        self.model = DecisionTreeClassifier(max_depth=4, random_state=42)
        self.model.fit(X, y)
        with open(self.model_path, 'wb') as file:
            pickle.dump(self.model, file)

    def _load_model(self):
        with open(self.model_path, 'rb') as file:
            self.model = pickle.load(file)

    def _evaluate_model(self, X, y):
        predictions = self.model.predict(X)
        self.accuracy = float(accuracy_score(y, predictions) * 100)
        self.confusion_matrix = confusion_matrix(y, predictions)

    def _save_visualizations(self):
        self._plot_confusion_matrix()

    def _plot_confusion_matrix(self):
        plt.figure(figsize=(7, 6))
        plt.imshow(self.confusion_matrix, interpolation='nearest', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.colorbar()
        tick_marks = np.arange(len(self.target_names))
        plt.xticks(tick_marks, self.target_names, rotation=45)
        plt.yticks(tick_marks, self.target_names)

        threshold = self.confusion_matrix.max() / 2.0
        for i in range(self.confusion_matrix.shape[0]):
            for j in range(self.confusion_matrix.shape[1]):
                plt.text(
                    j,
                    i,
                    format(self.confusion_matrix[i, j], 'd'),
                    horizontalalignment='center',
                    color='white' if self.confusion_matrix[i, j] > threshold else 'black'
                )

        plt.tight_layout()
        plt.ylabel('Actual Label')
        plt.xlabel('Predicted Label')
        output_path = os.path.join(self.output_dir, 'confusion_matrix.png')
        plt.savefig(output_path, dpi=120, bbox_inches='tight')
        plt.close()

    def _plot_decision_tree(self):
        plt.figure(figsize=(14, 10))
        plot_tree(
            self.model,
            feature_names=self.feature_names,
            class_names=self.target_names,
            filled=True,
            rounded=True,
            fontsize=10
        )
        plt.title('Decision Tree for Iris Classification')
        output_path = os.path.join(self.output_dir, 'decision_tree.png')
        plt.savefig(output_path, dpi=120, bbox_inches='tight')
        plt.close()

    def predict(self, values):
        """Predict the species from a list of four numeric measurements."""
        values_array = np.array(values, dtype=float).reshape(1, -1)
        index = int(self.model.predict(values_array)[0])
        return self.target_names[index]
