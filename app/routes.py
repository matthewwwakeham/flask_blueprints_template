import logging
from flask import Blueprint, session, request, render_template, url_for, redirect, flash
from datetime import datetime

proxy_bp = Blueprint('proxy', __name__)

@proxy_bp.route('/')
def index():
    logging.info(f"Home route accessed from {request.remote_addr} at {datetime.now()}")
    return render_template('index.html')