from flask import Blueprint

tb = Blueprint('tables', __name__, template_folder='../templates/table', static_folder='../static')

from app.tables.handlers import *
