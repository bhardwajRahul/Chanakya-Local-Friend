import logging
from flask import Flask
from flask_cors import CORS
import scripts.config as config

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)
app.secret_key = config.APP_SECRET_KEY

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

if not app.logger.handlers:
    app.logger.addHandler(log_handler)

app.logger.setLevel(logging.INFO)
app.logger.info("Flask app initialized and logger configured.")
