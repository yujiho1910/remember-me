# Standard Library imports

# Core Flask imports
from flask import render_template, redirect

# Third-party imports

# App imports

# Declare type


def index():
    return render_template('index.html')

def upload():
    return render_template('upload.html')
