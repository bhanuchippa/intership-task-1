document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('prediction-form');
  const resultText = document.getElementById('result-text');
  const accuracyText = document.getElementById('accuracy-value');
  const alertBox = document.getElementById('alert-box');
  const loader = document.getElementById('loading-indicator');
  const button = document.getElementById('predict-button');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    alertBox.textContent = '';

    const payload = {
      sepal_length: document.getElementById('sepal-length').value,
      sepal_width: document.getElementById('sepal-width').value,
      petal_length: document.getElementById('petal-length').value,
      petal_width: document.getElementById('petal-width').value,
    };

    if (Object.values(payload).some(value => value.trim() === '')) {
      alertBox.textContent = 'Please fill in all measurement fields before predicting.';
      return;
    }

    button.disabled = true;
    loader.classList.add('active');

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const result = await response.json();
      if (!result.success) {
        alertBox.textContent = result.error || 'Unable to generate prediction.';
      } else {
        resultText.textContent = result.predicted_species;
        accuracyText.textContent = result.accuracy;
      }
    } catch (error) {
      alertBox.textContent = 'Connection error. Please try again.';
    } finally {
      loader.classList.remove('active');
      button.disabled = false;
    }
  });
});
