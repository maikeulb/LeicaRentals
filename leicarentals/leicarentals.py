import os
from app import create_app, cli, celery

app = create_app(os.getenv('FLASK_APP_CONFIG') or 'config.DevelopmentConfig')
app.app_context().push()
cli.register(app)
