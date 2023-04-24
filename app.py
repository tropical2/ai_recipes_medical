import logging
import time
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def setup_logging():
    log_level = logging.DEBUG if app.debug else logging.INFO

    # Create a custom logger for the application
    logger = logging.getLogger("myapp")
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Log to a file with a rotating handler
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=1024 * 1024, backupCount=10)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Log to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

# Set up logging
setup_logging()


@app.route('/recipe-generator-en', methods=['GET'])
def recipe_generator_en():
    return render_template('recipe-generate-form-en.html')

@app.route('/submit-form-en', methods=['POST'])
def submit_form_en():
    # Extract the form data from the request
    dropdown_value = request.form.get('dropdown')
    text_input_value = request.form.get('text_input')

    # Process the form data (add your processing logic here)
    # This is just a simple example, replace it with your actual processing logic
    output = f'Processed data for condition {dropdown_value} and text input {text_input_value}'
    time.sleep(10)
    # Return the generated output text as a plain text response
    return output

if __name__ == '__main__':
    app.run(debug=True)
