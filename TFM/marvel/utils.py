import csv
import hashlib
import datetime
from flask import abort

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


def get_paginated_list(results, url, start, limit):
        start = int(start)
        limit = int(limit)
        count = len(results)
        if count < start or limit < 0:
            abort(404)

        obj = {}
        obj['start'] = start
        obj['limit'] = limit
        obj['count'] = count

        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(0, start - limit)
            limit_copy = start - 1
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)

        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)

        obj['results'] = results[(start - 1):(start - 1 + limit)]
        return obj

