# -*- coding: utf-8 -*-

import os
import logging
from flask import Flask, render_template
from logging import Formatter, StreamHandler
from werkzeug.contrib.cache import FileSystemCache

from utils import get_users

VERSION = "1.0.0"

app = Flask(__name__)
cache = FileSystemCache('/tmp')

# Configure logger
handler = StreamHandler()
FORMAT = '%(asctime)s [%(levelname)s] %(message)s '
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
if os.getenv('DEBUG', False):
    app.logger.setLevel(logging.DEBUG)

@app.route("/")
def home():
    """
    Homepage
    """

    # Set config
    config = {
        "cache": {
            "expiration": os.getenv('CACHE_EXPIRATION', 43200)
        }
        "page": {
            "message": os.getenv('PAGE_MESSAGE', 'Here is the team!'),
            "title": os.getenv('PAGE_TITLE', 'Slack phonebook'),
        },
        "show": {
            "user": {
                "email": os.getenv('SHOW_USER_EMAIL', True),
                "phone": os.getenv('SHOW_USER_PHONE', True),
                "title": os.getenv('SHOW_USER_TITLE', True),
                "vcard": os.getenv('SHOW_USER_VCARD', True),
            }
        },
        "version": VERSION,
    }

    # Get users
    users = cache.get('users')
    if users is None:
        users = get_users(app)
        cache.set('users', users, timeout=config.cache.expiration)

    return render_template('home.html', users=users, config=config)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)