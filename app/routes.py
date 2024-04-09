# Standard Library imports

# Core Flask imports
from flask import Flask

# Third-party imports

# App imports


def init_routes(app: Flask) -> None:
    from .views import static_views, error_views, public_apis, public_views

    # Public views
    app.add_url_rule("/", view_func=static_views.index)
    app.add_url_rule("/upload_auth", view_func=static_views.upload_auth)
    app.add_url_rule("/upload/<string:content_id>", view_func=public_views.upload)

    # Error views
    app.register_error_handler(404, error_views.not_found_error)
    app.register_error_handler(500, error_views.internal_error)

    # Public APIs
    app.add_url_rule("/api/login", methods=["POST"], view_func=public_apis.login)
    app.add_url_rule("/api/contact", methods=["POST"], view_func=public_apis.contact)

    # Admin APIs
