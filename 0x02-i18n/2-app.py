#!/usr/bin/env python3
"""
This module starts a Flask web application and renders a template on the root
route.

The application runs on host '0.0.0.0' and port 5000 with debug mode enabled.
"""

from flask import Flask, render_template
from flask_babel import Babel, request


app = Flask(__name__)


class Config:
    """
    Configuration class for setting application parameters.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best match for the client's preferred language.

    This function is used by Flask-Babel to determine which language to use
    for translations. It checks the languages preferred by the client (as
    indicated by the 'Accept-Language' header in the request) and matches
    them against the supported languages configured in the application.

    Returns:
        str: The best matching language code from the supported languages,
        or the default language if no match is found.
    """
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """
    Renders the '2-index.html' template on the root route.

    Returns:
        str: The rendered HTML content of the '1-index.html' template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    """
    Starts the Flask web application.

    The application will run in debug mode, listening on all available
    IP addresses on port 5000.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
