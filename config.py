import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """docstring for Config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-newer-guess'
    # WTF_CSRF_SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-pass'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0  # отключить кэш статик файлов JS CSS
