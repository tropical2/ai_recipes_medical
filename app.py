import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

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


@app.route('/recipe_generator_en', methods=['GET'])
def recipe_generator_en():
    return render_template('recipe_generate_form_en.html')

@app.route('/submit_form_en', methods=['POST'])
def submit_form_en():
    dropdown = request.form.get('dropdown')
    text_input = request.form.get('text_input')
    print(f'Dropdown: {dropdown}, Text Input: {text_input}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
