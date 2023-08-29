#!/usr/bin/env python3
"""Detremine user's preferred locale."""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """A class used to configure a Flask app."""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the most suitable locale."""
    preferred_langs = request.accept_languages
    return preferred_langs.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """Render a html template."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
