from flask import Blueprint

rentals = Blueprint('rentals', __name__)

from app.rentals import views
