from app import app, db
from app.models import User, Exchange, PrivatSettings


@app.shell_context_processor
def make_shell_context():
    result = {
        'db': db, 'User': User, 'Exchange': Exchange,
        'PrivatSettings': PrivatSettings
        }
    return result
