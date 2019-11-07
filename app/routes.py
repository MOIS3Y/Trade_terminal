# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from flask import request
from werkzeug.urls import url_parse
from app import app
from app import db
from app.models import User
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import SettingsForm
from app.models import Exchange, PrivatSettings


@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Index')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    # select = request.form.get('exchange')
    exchanges = Exchange.query.all()
    form = SettingsForm()
    form.select.choices = [(exchange.id, exchange.name) for exchange in exchanges]
    flash(form.select.choices)
    flash(form.validate_on_submit())
    if current_user.is_authenticated:
        pass

    if form.validate_on_submit():
        new_settings = PrivatSettings(
            user_id=current_user.id, exchange_id=form.select.data, name=form.name.data,
            secret_key=form.secret_key.data, public_key=form.public_key.data)
        flash(new_settings)
        db.session.add(new_settings)
        db.session.commit()
        flash('Смотри новые данные в базе!')

    privat_settings = PrivatSettings.query.filter_by(user_id=current_user.id).all()
    flash(privat_settings)

    return render_template(
        'settings.html',
        title='Settings',
        form=form,
        exchanges=exchanges,
        privat_settings=privat_settings)


@app.route('/service', methods=['POST'])
def _update():
    privat_settings = PrivatSettings.query.filter_by(user_id=current_user.id).all()
    return jsonify({'data': render_template('service.html', privat_settings=privat_settings)})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
