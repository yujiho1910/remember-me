# Standard Library imports

# Core Flask imports
from flask import render_template, redirect

# Third-party imports

# App imports

# Declare type


def upload(content_id):
    return render_template(f'upload.html', content_id=content_id)
