# Standard Library imports

# Core Flask imports
from flask import Flask

# Third-party imports
from sqlalchemy.orm import scoped_session

# App imports


def init_routes(app: Flask) -> None:
    from .views import (
        static_views,
        error_views,
    )

    # Public views
    app.add_url_rule('/', view_func=static_views.index)
    app.add_url_rule('/upload', view_func=static_views.upload)

    # Error views
    app.register_error_handler(404, error_views.not_found_error)
    app.register_error_handler(500, error_views.internal_error)

    # Public APIs

    # Admin APIs
