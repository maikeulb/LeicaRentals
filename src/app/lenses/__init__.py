from flask import Blueprint

lenses = Blueprint('lenses', __name__)

from app.lenses import views
