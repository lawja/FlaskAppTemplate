from flask import abort, jsonify, render_template, redirect
from manage import app
from . import main

@main.route('/')
def index():
    return render_template('index.html')