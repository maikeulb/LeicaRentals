@celery.task
def email_async_newsletter(msg):
    with app.app_context():
        mail.send(msg)
