# Standard Library imports

# Core Flask imports
from flask import Flask

# Third-party imports

# App imports
from app.routes import init_routes
from config import config_manager


# Load extensions


def create_app(env):
    '''
    Create Flask app with app factory pattern method. Client component

    :param env: Either dev/test/prod
    '''
    app = Flask(__name__)
    app.config.from_object(config_manager[env])

    init_routes(app)

    return app
