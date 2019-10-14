# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from app import app
from app import db
from app.models import User
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import SettingsForm


@app.route('/')
def index():
    return render_template('index.html', title='Index')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    return render_template('settings.html', title='Settings', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')
