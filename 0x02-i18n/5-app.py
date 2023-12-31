#!/usr/bin/env python3
"""Configure babel."""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)

babel = Babel(app)


class Config:
    """A class to configure a Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return a user dict."""
    key = request.args.get('login_as')
    return users[int(key)] if key and int(key) in users.keys() else None


@babel.localeselector
def get_locale():
    """Get user's preferred locale."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Set user attribute in the global object."""
    g.user = get_user()


@app.route('/')
def home():
    """Render a html template."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
