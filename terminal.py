from app import app, db
from app.models import User, Exchange, PrivateSettings


@app.shell_context_processor
def make_shell_context():
    result = {
        'db': db, 'User': User, 'Exchange': Exchange,
        'PrivateSettings': PrivateSettings
        }
    return result
