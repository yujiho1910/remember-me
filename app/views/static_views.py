# Standard Library imports

# Core Flask imports
from flask import render_template, redirect

# Third-party imports

# App imports

# Declare type


def index():
    return render_template('index.html')

def upload_auth():
    return render_template('upload_auth.html')
