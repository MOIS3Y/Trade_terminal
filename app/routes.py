# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask import request, jsonify
from werkzeug.urls import url_parse
from app import app
from app import db
from app.models import User
from app.forms import LoginForm
from app.models import Exchange, PrivateSettings


@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Index')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    exchanges = Exchange.query.all()
    # flash(exchanges)
    private_settings = PrivateSettings.query.filter_by(
        user_id=current_user.id).all()
    # flash(private_settings)

    return render_template(
        'settings.html',
        title='Settings',
        exchanges=exchanges,
        private_settings=private_settings)


@app.route('/update_accounts', methods=['POST'])
def _update():
    status = request.form['update']
    if status == 'create_account':
        new_settings = PrivateSettings(
            user_id=current_user.id,
            exchange_id=request.form['exchange_id'],
            name=request.form['name'],
            secret_key=request.form['secret_key'],
            public_key=request.form['public_key'])
        db.session.add(new_settings)
        db.session.commit()
    if status == 'delete_account':
        id_account = str(request.form['id_account'])
        delete_account = PrivateSettings.query.filter_by(
            id=id_account).first()
        db.session.delete(delete_account)
        db.session.commit()

    private_settings = PrivateSettings.query.filter_by(
        user_id=current_user.id).all()
    return jsonify(
        {
            'accounts': render_template(
                '_update_account_table.html',
                private_settings=private_settings),
            'status': status
        })


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
