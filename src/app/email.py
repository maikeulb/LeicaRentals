@celery.task
def send_async_newsletter(msg):
    with app.app_context():
        mail.send(msg)
