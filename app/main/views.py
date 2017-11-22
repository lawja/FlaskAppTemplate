from flask import (abort, jsonify, g, session, render_template, redirect,
                   request, url_for)
from manage import app#, client
from . import main

@main.route('/')
def index():
    return render_template('index.html')