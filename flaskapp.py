# Standard Library imports
import os
from dotenv import load_dotenv

# Core Flask imports

# Third-party imports

# App imports
from app import create_app


dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_ENV') or 'dev')

@app.shell_context_processor
def make_shell_context():
    return dict()
