from crypt import methods
from flask import render_template, request, session, redirect 

from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

