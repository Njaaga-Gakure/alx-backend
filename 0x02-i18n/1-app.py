#!/usr/bin/env python3
"""Configure babel."""


from flask import Flask, render_template, jsonify
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """A class to configure a Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


@app.route('/')
def home():
    """Render a html template."""
    return render_template('1-index.html')


@app.route('/languages')
def languages():
    """Check languages."""
    return jsonify(languages=app.config['LANGUAGES'])


@app.route('/default_locale')
def default_locale():
    """Check default locale."""
    return jsonify(default_locale=app.config['BABEL_DEFAULT_LOCALE'])


@app.route('/default_timezone')
def default_timezone():
    """Check default timezone."""
    return jsonify(default_timezone=app.config['BABEL_DEFAULT_TIMEZONE'])


if __name__ == '__main__':
    app.run()
