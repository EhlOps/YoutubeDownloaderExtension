from flask import Flask, logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["chrome-extension://*"])
logger = logging.create_logger(app)
logger.setLevel("INFO")
