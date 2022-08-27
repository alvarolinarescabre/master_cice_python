import requests
from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_args
from marvel.utils import hash_params, timestamp, pub_key
from marvel.models import Battle


marvel = Blueprint("marvel", __name__, template_folder="templates", static_folder="static")

# Marvel's Info
url = "https://gateway.marvel.com:443/v1/public/characters"


@marvel.get("/")
def index():
    return render_template("index.html")


@marvel.get("/heroes/")
def heroes():
    data_page = request.args.get('page', default=0, type=int)
    start = 24 * data_page
    params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    data = requests.get(f'{url}?offset={start}&limit=24', params=params).json()
    results = data.get("data").get("results")
    total = 500 # Only first 500 heroes

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap5')

    return render_template('heroes.html',
                           heroes=results,
                           page=page,
                           per_page=24,
                           pagination=pagination,
                           )


@marvel.get("/heroe/<int:character_id>")
def heroe(character_id):
    params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    data = requests.get(f'{url}/{character_id}', params=params).json()
    results = data.get("data").get("results")

    return render_template('heroe.html', heroe=results)


@marvel.route("/battle/", methods=["GET", "POST"])
def battle():
    if request.method == "GET":
        results = Battle.query.order_by(Battle.name).all()
        return render_template('battle.html', heroes=results)
    elif request.method == "POST":
        heroe_id = request.form.get("heroes")
        villain_id = request.form.get("villains")

        heroe_data = Battle.query.filter_by(id=heroe_id).first()
        villain_data = Battle.query.filter_by(id=villain_id).first()

        return render_template('battle.html', heroe=heroe_data, villain=villain_data)
