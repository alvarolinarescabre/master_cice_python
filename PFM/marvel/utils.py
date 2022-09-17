import hashlib
import datetime
import functools
from flask import session, redirect, url_for, abort
from marvel.models import Users

# Variables for Marvel's API Hash
timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
priv_key = '697c5b76886b235941f0a44fed58381e65c924fa'
pub_key = 'a0468af2bab822d80e858a3a7312a0a8'


def hash_params():
    """ La API de Marvel API necesita incluir lo siguiente:
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        email = session.get("email")
        if email or email in Users.query.all():
            redirect(url_for("marvel.home"))
        else:
            abort(401)

        return route(*args, **kwargs)
    return route_wrapper
