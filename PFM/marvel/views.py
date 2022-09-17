import requests
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, render_template, request, session, flash
from flask_paginate import Pagination, get_page_args
from marvel.utils import hash_params, timestamp, pub_key, login_required
from marvel import db
from marvel.models import Battle, Users

marvel = Blueprint("marvel", __name__, template_folder="templates", static_folder="static")

# Marvel's Info
url = "https://gateway.marvel.com:443/v1/public/characters"


@marvel.route("/", methods=["GET", "POST"])
def index():
    email = request.form.get("email")
    password = request.form.get("password")
    user = Users.query.filter_by(email=email).first()

    if request.method == "GET":
        if not user:
            return render_template("signup.html")
    elif request.method == "POST":
        if pbkdf2_sha256.verify(password, user.password):
            flash(f"¡Welcome again, {user.email}!")
            session["email"] = email
            return render_template("home.html")
        else:
            flash("¡Please enter the correct email and/or password!")

    return render_template("index.html")


@marvel.route("/signup", methods=["GET", "POST"])
def signup():
    email = request.form.get("email")
    password = request.form.get("password")

    if email and password:
        try:
            db.session.add(Users(email=email, password=pbkdf2_sha256.hash(password)))
            db.session.commit()
            flash("¡Successfully registred!")
        except IntegrityError:
            flash("¡The user is exists!")

    return render_template("index.html")


@marvel.get("/logout")
@login_required
def logout():
    session.clear()
    return render_template("index.html")


@marvel.get("/home")
@login_required
def home():
    return render_template("home.html")


@marvel.get("/heroes/")
@login_required
def heroes():
    data_page = request.args.get('page', default=0, type=int)
    start = 14 * data_page
    params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    data = requests.get(f'{url}?offset={start}&limit=14', params=params).json()
    results = data.get("data").get("results")
    total = 500 # Only first 500 heroes

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap5')

    return render_template('heroes.html',
                           heroes=results,
                           page=page,
                           per_page=14,
                           pagination=pagination,
                           )


@marvel.get("/heroe/<int:character_id>")
@login_required
def heroe(character_id):
    params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    data = requests.get(f'{url}/{character_id}', params=params).json()
    results = data.get("data").get("results")

    return render_template('heroe.html', heroe=results)


@marvel.route("/battle/", methods=["GET", "POST"])
@login_required
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


@marvel.errorhandler(401)
def page_not_authorized(e):
    return render_template('401.html'), 401
