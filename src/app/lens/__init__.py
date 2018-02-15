from flask import Blueprint

lens = Blueprint('lens', __name__)

from app.lens import views
