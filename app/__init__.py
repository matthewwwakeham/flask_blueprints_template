import os
import logging
from flask import Flask
from dotenv import load_dotenv
from app.routes import proxy_bp

load_dotenv(dotenv_path='variables/.env')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(proxy_bp, url_prefix='/')

    setup_logging()

    return app

def setup_logging():
    """Sets up global logging for the app."""
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure file logging
    logging.basicConfig(
        filename='logs/global.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Configure console logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Add console handler to the root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)