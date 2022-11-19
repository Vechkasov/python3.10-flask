# -*- coding: utf-8 -*-
from flask import render_template, url_for, flash, redirect
from app import app
from app.models import *


# Get all notifications
@app.context_processor
def context_processor():
    return dict(notifications=Notifications.query.order_by(Notifications.date.desc()).all())


# Delete all notifications
@app.route('/notifications/delete')
def delete_notifications():
    for item in Notifications.query.all():
        db.session.delete(item)
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
