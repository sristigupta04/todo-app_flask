from flask import Blueprint,render_template,request,redirect,url_for,flash,session

from app import db
from app.models import Task

tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))